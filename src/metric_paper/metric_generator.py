from dataclasses import dataclass
import numpy as np
import sympy as sp


@dataclass(frozen=True)
class Coefficients:
    theta: np.ndarray
    lam: np.ndarray

    def __post_init__(self):
        if len(self.theta) != 4 or len(self.lam) != 4:
            raise ValueError("theta and lambda must have 4 elements")


def _as_sympy_coeffs(values):
    out = []
    for v in values:
        if isinstance(v, (int, sp.Integer)):
            out.append(sp.Integer(v))
        else:
            try:
                iv = int(v)
                if float(v) == iv:
                    out.append(sp.Integer(iv))
                else:
                    out.append(sp.Rational(v))
            except Exception:
                out.append(sp.Rational(v))
    return out


def eta_expression(theta, lam):
    if len(theta) != 4 or len(lam) != 4:
        raise ValueError("theta and lambda must have 4 elements")
    th = _as_sympy_coeffs(theta)
    la = _as_sympy_coeffs(lam)
    TP, FN, FP, TN = sp.symbols("TP FN FP TN")
    num = th[0]*TP + th[1]*FN + th[2]*FP + th[3]*TN
    den = la[0]*TP + la[1]*FN + la[2]*FP + la[3]*TN
    expr = sp.simplify(sp.cancel(num/den))
    return sp.Eq(sp.symbols("eta"), expr)


def eta_string(theta, lam):
    return str(eta_expression(theta, lam))
