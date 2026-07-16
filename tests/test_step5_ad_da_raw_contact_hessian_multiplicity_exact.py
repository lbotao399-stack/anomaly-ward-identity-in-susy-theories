import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "step5_ad_da_raw_contact_hessian_multiplicity_exact_audit.py"
ARTIFACT = ROOT / "audits" / "step5-ad-da-raw-contact-hessian-multiplicity-exact.json"


def load_module():
    spec = importlib.util.spec_from_file_location("ad_da_raw_contact", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class TestADDAContactHessianMultiplicity(unittest.TestCase):
    def test_artifact(self):
        module = load_module()
        payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        module.validate(payload)
        self.assertEqual(payload["local_w0"]["m_contact"], "1")
        self.assertEqual(payload["normalization_consequence"]["raw_contact_half"], "REJECTED")
        self.assertEqual(payload["checks"]["failed"], 0)


if __name__ == "__main__":
    unittest.main()
