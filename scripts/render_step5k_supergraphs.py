#!/usr/bin/env python3
"""Render the Step-5K triangles; checks primary-memo equations (K.47)--(K.48)."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
import re
import shutil
import subprocess
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IR_PATH = ROOT / "audits" / "step5k-diagram-ir.json"
OUT_DIR = ROOT / "paper" / "figures"
SVG_NUMBER = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
SVG_PATH_TOKEN = re.compile(rf"{SVG_NUMBER}|[A-Za-z]")
SVG_TRANSFORM = re.compile(r"([A-Za-z]+)\s*\(([^)]*)\)")
TOPOLOGY_ROLE_COUNTS = Counter(
    {
        "insertion_outer": 1,
        "insertion_inner": 1,
        "action_vertex": 2,
        "propagator": 4,
        "marked_edge_outer": 1,
        "marked_edge_inner": 1,
        "momentum_shaft": 3,
        "momentum_head": 3,
    }
)
TOPOLOGY_COORDINATE_TOLERANCE = 2.0e-4
TOPOLOGY_FRAME_TOLERANCE = 2.0e-2


def graph_by_id(graph_id: str) -> dict[str, object]:
    data = json.loads(IR_PATH.read_text(encoding="utf-8"))
    return next(graph for graph in data["graphs"] if graph["id"] == graph_id)


def vertex(graph: dict[str, object], vertex_id: str) -> dict[str, object]:
    return next(item for item in graph["vertices"] if item["id"] == vertex_id)


def edge(graph: dict[str, object], edge_id: str) -> dict[str, object]:
    return next(item for item in graph["internal_edges"] if item["id"] == edge_id)


def external(graph: dict[str, object], vertex_id: str) -> dict[str, object]:
    return next(item for item in graph["external_legs"] if item["at"] == vertex_id)


def validate_graph_topology(
    graph: dict[str, object],
    left_id: str,
    right_id: str,
) -> None:
    """Bind the typed IR endpoints to the three paths drawn by TikZ."""
    vertex_ids = [item["id"] for item in graph["vertices"]]
    edge_endpoints = {
        item["id"]: (item["from"], item["to"])
        for item in graph["internal_edges"]
    }
    external_attachments = Counter(item["at"] for item in graph["external_legs"])
    expected_edges = {
        "e0": ("I", left_id),
        "e1": (left_id, right_id),
        "e2": (right_id, "I"),
    }
    failures: list[str] = []
    if Counter(vertex_ids) != Counter({"I": 1, left_id: 1, right_id: 1}):
        failures.append(f"vertices={vertex_ids!r}")
    if len(graph["internal_edges"]) != 3 or edge_endpoints != expected_edges:
        failures.append(f"edges={edge_endpoints!r}")
    if external_attachments != Counter({left_id: 1, right_id: 1}):
        failures.append(f"external={dict(external_attachments)!r}")
    e2 = next(
        (item for item in graph["internal_edges"] if item["id"] == "e2"),
        None,
    )
    if e2 is None or "e^{iw\\cdot r_2}" not in e2["propagator_tex"]:
        failures.append("e2 is not the phase-marked edge")
    if failures:
        raise ValueError(f"invalid diagram IR topology for {graph['id']}: " + "; ".join(failures))


def figure_tex(graph: dict[str, object]) -> str:
    is_gauge = graph["sector"] == "GAUGE_VECTOR"
    left_id = "VBAR" if is_gauge else "MC"
    right_id = "VW" if is_gauge else "MB"
    validate_graph_topology(graph, left_id, right_id)
    left = vertex(graph, left_id)
    right = vertex(graph, right_id)
    insertion = vertex(graph, "I")
    e0 = edge(graph, "e0")
    e1 = edge(graph, "e1")
    e2 = edge(graph, "e2")
    ext_left = external(graph, left_id)
    ext_right = external(graph, right_id)
    graph_id = graph["id"]
    title = graph["title_tex"]
    source_word = graph["source_word_tex"]
    denominator = graph["denominator"].replace("*", r"\,")

    left_vertex = left["label_tex"]
    right_vertex = right["label_tex"]
    e0_label = rf"{e0['field_tex']},\quad {e0['momentum_tex']}"
    e1_label = rf"{e1['field_tex']},\quad {e1['momentum_tex']}"
    e2_label = rf"{e2['field_tex']},\quad {e2['momentum_tex']},\quad e^{{iw\cdot r_2}}"

    return rf"""\documentclass[tikz,border=8pt]{{standalone}}
\usepackage{{amsmath,amssymb}}
\usetikzlibrary{{arrows.meta,calc,positioning,shapes.geometric}}
\begin{{document}}
\begin{{tikzpicture}}[
  >=Stealth,
  momentum/.style={{-{{Stealth[length=2mm]}},line width=0.65pt}},
  propagator/.style={{line width=0.85pt}},
  insertion/.style={{diamond,draw,double,inner sep=2.5pt,minimum size=10mm}},
  action/.style={{circle,fill=black,inner sep=2.6pt}},
  formula/.style={{draw=black!30,rounded corners=1.5pt,fill=white,inner sep=4pt,align=center}},
  every node/.style={{font=\small}}
]
\node[font=\bfseries] at (0,4.55) {{$\displaystyle {title}$}};
\node[insertion] (I) at (0,-1.75) {{$\displaystyle {insertion['label_tex']}$}};
\node[action] (L) at (-3.0,1.55) {{}};
\node[action] (R) at (3.0,1.55) {{}};

\draw[propagator] (I) -- (L)
  node[pos=.45,sloped,above] {{$\displaystyle {e0_label}$}};
\draw[propagator] (L) -- (R)
  node[midway,above=3pt] {{$\displaystyle {e1_label}$}};
\draw[propagator,double distance=1.2pt] (R) -- (I)
  node[pos=.53,sloped,below=3pt] {{$\displaystyle {e2_label}$}};

\draw[momentum] ($(I)!0.18!(L)$) -- ($(I)!0.38!(L)$);
\draw[momentum] ($(L)!0.38!(R)$) -- ($(L)!0.58!(R)$);
\draw[momentum] ($(R)!0.18!(I)$) -- ($(R)!0.38!(I)$);

\draw[propagator] (-5.25,2.75) -- (L)
  node[pos=.03,above right] {{$\displaystyle {ext_left['label_tex']}$}};
\draw[propagator] (R) -- (5.25,2.75)
  node[pos=.97,above left] {{$\displaystyle {ext_right['label_tex']}$}};

\node[formula,anchor=east] at (-3.35,.15)
  {{$\displaystyle {left_vertex}$}};
\node[formula,anchor=west] at (3.35,.15)
  {{$\displaystyle {right_vertex}$}};

\node[formula,text width=13.6cm] at (0,-3.45)
  {{$\displaystyle {source_word}$\\[2pt]
   $\displaystyle {denominator}$}};
\node[font=\ttfamily\footnotesize] at (0,-4.45) {{{graph_id}}};
\end{{tikzpicture}}
\end{{document}}
"""


def outputs() -> list[tuple[str, str]]:
    return [
        ("G-WW-GAUGE-01", "step5k-gauge-vector-triangle"),
        ("G-WW-MATTER-01", "step5k-adjoint-matter-triangle"),
    ]


def emit_tex(check: bool = False) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    for graph_id, stem in outputs():
        expected = figure_tex(graph_by_id(graph_id))
        path = OUT_DIR / f"{stem}.tex"
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                failures.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding="utf-8")
    if failures:
        raise SystemExit("stale generated TeX: " + ", ".join(failures))


def compile_outputs(source: Path) -> tuple[bytes, bytes]:
    stem = source.stem
    with tempfile.TemporaryDirectory(prefix=f"{stem}-") as temporary:
        work = Path(temporary)
        staged = work / source.name
        shutil.copy2(source, staged)
        environment = os.environ.copy()
        environment["SOURCE_DATE_EPOCH"] = "1"
        environment["FORCE_SOURCE_DATE"] = "1"
        subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                staged.name,
            ],
            cwd=work,
            env=environment,
            check=True,
            capture_output=True,
            text=True,
        )
        pdf = work / f"{stem}.pdf"
        svg = work / f"{stem}.svg"
        subprocess.run(
            ["pdftocairo", "-svg", str(pdf), str(svg)],
            cwd=work,
            env=environment,
            check=True,
            capture_output=True,
            text=True,
        )
        return pdf.read_bytes(), svg.read_bytes()


def normalized_pdf_text(payload: bytes) -> str:
    with tempfile.TemporaryDirectory(prefix="step5k-pdf-text-") as temporary:
        pdf = Path(temporary) / "figure.pdf"
        pdf.write_bytes(payload)
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            check=True,
            capture_output=True,
            text=True,
        )
    return " ".join(unicodedata.normalize("NFKC", result.stdout).split())


def pdf_to_svg(payload: bytes) -> bytes:
    """Normalize PDF drawing operators through the checker host's Poppler."""
    with tempfile.TemporaryDirectory(prefix="step5k-pdf-svg-") as temporary:
        work = Path(temporary)
        pdf = work / "figure.pdf"
        svg = work / "figure.svg"
        pdf.write_bytes(payload)
        subprocess.run(
            ["pdftocairo", "-svg", str(pdf), str(svg)],
            cwd=work,
            check=True,
            capture_output=True,
            text=True,
        )
        return svg.read_bytes()


def _compose_affine(
    outer: tuple[float, float, float, float, float, float],
    inner: tuple[float, float, float, float, float, float],
) -> tuple[float, float, float, float, float, float]:
    """Return the affine map outer(inner(point))."""
    oa, ob, oc, od, oe, of = outer
    ia, ib, ic, id_, ie, iff = inner
    return (
        oa * ia + oc * ib,
        ob * ia + od * ib,
        oa * ic + oc * id_,
        ob * ic + od * id_,
        oa * ie + oc * iff + oe,
        ob * ie + od * iff + of,
    )


def _parse_transform(value: str | None) -> tuple[float, float, float, float, float, float]:
    identity = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    if not value:
        return identity
    result = identity
    position = 0
    for match in SVG_TRANSFORM.finditer(value):
        if value[position : match.start()].strip(" ,\t\r\n"):
            raise ValueError(f"unsupported SVG transform syntax: {value!r}")
        name = match.group(1)
        numbers = [float(item) for item in re.findall(SVG_NUMBER, match.group(2))]
        if name == "matrix" and len(numbers) == 6:
            operation = tuple(numbers)
        elif name == "translate" and len(numbers) in (1, 2):
            tx = numbers[0]
            ty = numbers[1] if len(numbers) == 2 else 0.0
            operation = (1.0, 0.0, 0.0, 1.0, tx, ty)
        elif name == "scale" and len(numbers) in (1, 2):
            sx = numbers[0]
            sy = numbers[1] if len(numbers) == 2 else sx
            operation = (sx, 0.0, 0.0, sy, 0.0, 0.0)
        else:
            raise ValueError(f"unsupported SVG transform: {match.group(0)!r}")
        result = _compose_affine(result, operation)
        position = match.end()
    if value[position:].strip(" ,\t\r\n"):
        raise ValueError(f"unsupported SVG transform syntax: {value!r}")
    return result


def _transform_point(
    matrix: tuple[float, float, float, float, float, float],
    point: tuple[float, float],
) -> tuple[float, float]:
    a, b, c, d, e, f = matrix
    x, y = point
    return a * x + c * y + e, b * x + d * y + f


def _path_geometry(
    value: str,
    matrix: tuple[float, float, float, float, float, float],
) -> tuple[str, list[tuple[float, float]]]:
    """Canonicalize the M/L/C/Z subset emitted by pdftocairo."""
    residue = SVG_PATH_TOKEN.sub("", value).replace(",", "")
    if residue.strip():
        raise ValueError(f"unparsed SVG path syntax: {residue!r}")
    tokens = SVG_PATH_TOKEN.findall(value)
    commands: list[str] = []
    points: list[tuple[float, float]] = []
    current = (0.0, 0.0)
    subpath_start = current
    command: str | None = None
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token.isalpha():
            command = token
            index += 1
            if command.upper() == "Z":
                commands.append("Z")
                current = subpath_start
                command = None
                continue
        if command is None:
            raise ValueError(f"SVG path has coordinates without a command: {value!r}")
        upper = command.upper()
        relative = command.islower()
        arity = {"M": 2, "L": 2, "C": 6}.get(upper)
        if arity is None or index + arity > len(tokens):
            raise ValueError(f"unsupported or truncated SVG path command {command!r}")
        if any(item.isalpha() for item in tokens[index : index + arity]):
            raise ValueError(f"truncated SVG path command {command!r}")
        values = [float(item) for item in tokens[index : index + arity]]
        index += arity
        base_x, base_y = current
        local_points: list[tuple[float, float]] = []
        for offset in range(0, arity, 2):
            x, y = values[offset], values[offset + 1]
            if relative:
                x += base_x
                y += base_y
            local_points.append((x, y))
        commands.append(upper)
        points.extend(_transform_point(matrix, point) for point in local_points)
        current = local_points[-1]
        if upper == "M":
            subpath_start = current
            command = "l" if relative else "L"
    if not points:
        raise ValueError("empty structural SVG path")
    return "".join(commands), points


def _parse_rgb(value: str | None) -> tuple[float, float, float] | None:
    if value is None or value == "none":
        return None
    named = {"black": (0.0, 0.0, 0.0), "white": (1.0, 1.0, 1.0)}
    if value in named:
        return named[value]
    match = re.fullmatch(
        r"rgb\(\s*([-+0-9.]+)(%)?\s*,\s*([-+0-9.]+)(%)?\s*,\s*([-+0-9.]+)(%)?\s*\)",
        value,
    )
    if match is None:
        raise ValueError(f"unsupported SVG color: {value!r}")
    channels = []
    for number, percent in ((match.group(1), match.group(2)), (match.group(3), match.group(4)), (match.group(5), match.group(6))):
        channel = float(number)
        channels.append(channel / 100.0 if percent else channel / 255.0)
    return tuple(channels)


def _near_color(
    actual: tuple[float, float, float] | None,
    expected: tuple[float, float, float],
) -> bool:
    return actual is not None and max(abs(left - right) for left, right in zip(actual, expected)) < 0.02


def _topology_role(style: dict[str, str]) -> str | None:
    fill_value = style.get("fill", "black")
    stroke_value = style.get("stroke", "none")
    fill = _parse_rgb(fill_value)
    stroke = _parse_rgb(stroke_value)
    width = float(style.get("stroke-width", "0"))
    black = (0.0, 0.0, 0.0)
    white = (1.0, 1.0, 1.0)
    if _near_color(fill, black) and stroke is None:
        return "action_vertex"
    if _near_color(fill, black) and _near_color(stroke, black) and 0.5 <= width < 0.75:
        return "momentum_head"
    if fill_value == "none" and _near_color(stroke, black):
        if 0.5 <= width < 0.75:
            return "momentum_shaft"
        if 0.75 <= width < 1.1:
            return "propagator"
        if 1.1 <= width < 2.1:
            return "insertion_outer"
        if width >= 2.1:
            return "marked_edge_outer"
    if fill_value == "none" and _near_color(stroke, white):
        if 0.45 <= width < 0.9:
            return "insertion_inner"
        if width >= 0.9:
            return "marked_edge_inner"
    return None


def svg_topology(payload: bytes) -> dict[str, object]:
    """Extract font-independent, affine-normalized graph ink from an SVG."""
    root = ET.fromstring(payload)
    viewbox_values = [float(item) for item in root.attrib.get("viewBox", "").split()]
    if len(viewbox_values) != 4:
        raise ValueError("SVG has no four-component viewBox")
    view_x, view_y, view_width, view_height = viewbox_values
    if view_width < 400.0 or view_height < 200.0:
        raise ValueError(f"cropped SVG viewport {viewbox_values!r}")

    raw_features: list[dict[str, object]] = []

    def walk(
        element: ET.Element,
        parent_matrix: tuple[float, float, float, float, float, float],
        parent_style: dict[str, str],
    ) -> None:
        local_name = element.tag.rsplit("}", 1)[-1]
        if local_name in {"defs", "use"}:
            return
        matrix = _compose_affine(parent_matrix, _parse_transform(element.attrib.get("transform")))
        style = dict(parent_style)
        for key in ("fill", "stroke", "stroke-width", "stroke-dasharray", "stroke-linecap", "stroke-linejoin"):
            if key in element.attrib:
                style[key] = element.attrib[key]
        if local_name == "path":
            role = _topology_role(style)
            if role is not None:
                commands, points = _path_geometry(element.attrib["d"], matrix)
                raw_features.append({"role": role, "commands": commands, "points": points})
        for child in element:
            walk(child, matrix, style)

    walk(root, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0), {"fill": "black", "stroke": "none"})
    role_counts = Counter(item["role"] for item in raw_features)
    if role_counts != TOPOLOGY_ROLE_COUNTS:
        raise ValueError(
            f"structural path contract mismatch: actual={dict(role_counts)!r}, "
            f"expected={dict(TOPOLOGY_ROLE_COUNTS)!r}"
        )
    all_points = [point for item in raw_features for point in item["points"]]
    min_x = min(point[0] for point in all_points)
    max_x = max(point[0] for point in all_points)
    min_y = min(point[1] for point in all_points)
    max_y = max(point[1] for point in all_points)
    width = max_x - min_x
    height = max_y - min_y
    if width <= 0.0 or height <= 0.0:
        raise ValueError("degenerate structural SVG bounding box")
    frame = (
        (min_x - view_x) / view_width,
        (min_y - view_y) / view_height,
        (max_x - view_x) / view_width,
        (max_y - view_y) / view_height,
    )
    if min(frame) < -1.0e-3 or max(frame) > 1.001:
        raise ValueError(f"structural graph is outside SVG viewport: frame={frame!r}")
    features: list[dict[str, object]] = []
    for item in raw_features:
        points = tuple(((x - min_x) / width, (y - min_y) / height) for x, y in item["points"])
        centroid = (
            sum(point[0] for point in points) / len(points),
            sum(point[1] for point in points) / len(points),
        )
        features.append(
            {
                "role": item["role"],
                "commands": item["commands"],
                "points": points,
                "centroid": centroid,
            }
        )
    features.sort(key=lambda item: (item["role"], item["centroid"][0], item["centroid"][1]))
    return {"features": features, "frame": frame, "role_counts": role_counts}


def assert_same_svg_topology(actual: bytes, expected: bytes, label: str) -> None:
    actual_topology = svg_topology(actual)
    expected_topology = svg_topology(expected)
    for left, right in zip(actual_topology["frame"], expected_topology["frame"]):
        if abs(left - right) > TOPOLOGY_FRAME_TOLERANCE:
            raise ValueError(f"{label}: structural viewport frame differs")
    actual_features = actual_topology["features"]
    expected_features = expected_topology["features"]
    if len(actual_features) != len(expected_features):
        raise ValueError(f"{label}: structural path count differs")
    for index, (left, right) in enumerate(zip(actual_features, expected_features)):
        if left["role"] != right["role"] or left["commands"] != right["commands"]:
            raise ValueError(f"{label}: structural path {index} role/command differs")
        left_points = left["points"]
        right_points = right["points"]
        if len(left_points) != len(right_points):
            raise ValueError(f"{label}: structural path {index} point count differs")
        maximum_error = max(
            max(abs(lx - rx), abs(ly - ry))
            for (lx, ly), (rx, ry) in zip(left_points, right_points)
        )
        if maximum_error > TOPOLOGY_COORDINATE_TOLERANCE:
            raise ValueError(
                f"{label}: structural path {index} geometry differs by {maximum_error:.8f}"
            )


def self_check_svg_topology_comparator(expected: bytes) -> None:
    """Prove that serialization noise passes and deletion of graph ink fails."""
    harmless = expected.replace(b"<svg ", b"<svg\n ", 1)
    assert_same_svg_topology(harmless, expected, "normalization self-check")
    if b"</defs>" not in expected:
        raise ValueError("topology self-check requires a defs boundary")
    prefix, body = expected.split(b"</defs>", 1)
    mutated_body, replacements = re.subn(rb"<path\b[^>]*/>", b"", body, count=1)
    if replacements != 1:
        raise ValueError("topology self-check could not remove a structural path")
    try:
        assert_same_svg_topology(prefix + b"</defs>" + mutated_body, expected, "deletion self-check")
    except ValueError:
        return
    raise ValueError("topology comparator accepted a deleted structural path")


def render() -> None:
    emit_tex(check=False)
    for _, stem in outputs():
        source = OUT_DIR / f"{stem}.tex"
        pdf_bytes, svg_bytes = compile_outputs(source)
        (OUT_DIR / f"{stem}.pdf").write_bytes(pdf_bytes)
        (OUT_DIR / f"{stem}.svg").write_bytes(svg_bytes)


def check() -> None:
    emit_tex(check=True)
    for _, stem in outputs():
        source = OUT_DIR / f"{stem}.tex"
        pdf = OUT_DIR / f"{stem}.pdf"
        svg = OUT_DIR / f"{stem}.svg"
        if not pdf.is_file() or pdf.stat().st_size < 1000:
            raise SystemExit(f"missing or empty {pdf.relative_to(ROOT)}")
        if not svg.is_file() or "<path" not in svg.read_text(encoding="utf-8"):
            raise SystemExit(f"missing formula paths in {svg.relative_to(ROOT)}")
        expected_pdf, expected_svg = compile_outputs(source)
        if normalized_pdf_text(pdf.read_bytes()) != normalized_pdf_text(expected_pdf):
            raise SystemExit(f"stale rendered formula content for {stem}")
        try:
            self_check_svg_topology_comparator(expected_svg)
            assert_same_svg_topology(svg.read_bytes(), expected_svg, f"{stem} SVG")
            assert_same_svg_topology(
                pdf_to_svg(pdf.read_bytes()),
                expected_svg,
                f"{stem} PDF",
            )
        except (ET.ParseError, ValueError) as error:
            raise SystemExit(f"stale rendered graph topology for {stem}: {error}") from error
    print(
        "PASS STEP5K_FORMULA_RENDERED_SUPERGRAPHS "
        "topology=IR+PDF+SVG memo=(K.47)--(K.48)"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.render:
        render()
    elif args.check:
        check()
    else:
        emit_tex(check=False)


if __name__ == "__main__":
    main()
