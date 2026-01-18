import sympy as sp


def build_equation(a, b, variable_name):
    x = sp.symbols(variable_name)
    y = sp.symbols("y")
    expr = a * x + b
    return sp.Eq(y, expr)
