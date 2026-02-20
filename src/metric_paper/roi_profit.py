from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class RoiParams:
    L: float
    U: float

    def __post_init__(self):
        if not (self.U > self.L):
            raise ValueError("Require U > L")
        if self.L <= 0:
            raise ValueError("Require L > 0")


def uniform_cdf(x, params):
    x_arr = np.asarray(x, dtype=float)
    return np.clip((x_arr - params.L) / (params.U - params.L), 0.0, 1.0)


def expected_inv_uniform(params):
    return (np.log(params.U) - np.log(params.L)) / (params.U - params.L)


def p_loss_roi(eta, params):
    return 1.0 - uniform_cdf(eta, params)


def expected_roi(eta, params):
    return eta * expected_inv_uniform(params) - 1.0


def worst_roi(eta, params):
    return eta / params.U - 1.0
