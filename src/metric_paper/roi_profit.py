from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RoiProfitParams:
    L: float
    U: float
    N_max: int
    V: float

    def __post_init__(self):
        if not (self.U > self.L):
            raise ValueError("Require U > L")
        if self.L <= 0:
            raise ValueError("Require L > 0")
        if self.N_max <= 0:
            raise ValueError("Require N_max > 0")

    def mean(self):
        return 0.5 * (self.L + self.U)

    def expected_inv(self):
        return (np.log(self.U) - np.log(self.L)) / (self.U - self.L)


@dataclass(frozen=True)
class ProfitModel:
    eta: float
    N: int


class FlipProbability:
    def __init__(self, params, tie_value=0.0):
        self.params = params
        self.tie_value = tie_value

    def p_flip(self, model_a, model_b):
        base = np.sign(model_a.eta - model_b.eta)
        if base == 0:
            return self.tie_value
        if model_a.N == model_b.N:
            return 0.0
        x_star = intersection_ipv(model_a, model_b)
        p = uniform_cdf(x_star, self.params)
        if base > 0:
            return p if model_a.N > model_b.N else 1.0 - p
        return 1.0 - p if model_a.N > model_b.N else p


def uniform_cdf(x, params):
    x_arr = np.asarray(x, dtype=float)
    return np.clip((x_arr - params.L) / (params.U - params.L), 0.0, 1.0)


def roi(eta, ipv_act):
    return eta / ipv_act - 1.0


def profit(model, ipv_act, params):
    return model.N * params.V * (model.eta - ipv_act)


def p_loss_roi(eta, params):
    return 1.0 - uniform_cdf(eta, params)


def expected_roi(eta, params):
    return eta * params.expected_inv() - 1.0


def worst_roi(eta, params):
    return eta / params.U - 1.0


def expected_profit(model, params):
    return model.N * params.V * (model.eta - params.mean())


def worst_profit(model, params):
    return model.N * params.V * (model.eta - params.U)


def intersection_ipv(model_a, model_b):
    denom = model_a.N - model_b.N
    if denom == 0:
        return np.nan
    return (model_a.N * model_a.eta - model_b.N * model_b.eta) / denom
