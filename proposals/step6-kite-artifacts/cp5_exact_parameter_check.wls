(* Exact projective integrals for memo equation (CP5.12). *)
Clear[a, b, c, U, f1, f2, f12, triangle];
c = 1 - a - b;
U = a b + c (a + b);
f1 = a (a (b + c)/6 + b c/2);
f2 = b (b (a + c)/6 + a c/2);
f12 = a b c/2;

triangle[expr_] := FullSimplify[
  Integrate[
    FullSimplify[
      Integrate[expr, {b, 0, 1 - a}, GenerateConditions -> False],
      0 < a < 1
    ],
    {a, 0, 1}, GenerateConditions -> False
  ]
];

i4 = triangle[a b c/U^3];
iS1 = triangle[a b c^2 f1/U^5];
iS2 = triangle[a b c^2 f2/U^5];
iS12 = triangle[a b c^2 f12/U^5];

Print["PASS (CP5.12) I4 = ", i4];
Print["PASS (CP5.12) I_C2 coefficients = ", {iS1, iS2, iS12}];
If[! TrueQ[i4 == 1/2 && iS1 == 1/24 && iS2 == 1/24 && iS12 == 1/48],
  Exit[1]
];
