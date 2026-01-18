from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ConfusionGrid:
    tp: np.ndarray
    fp: np.ndarray
    tn: np.ndarray
    fn: np.ndarray
    total: int


@dataclass(frozen=True)
class ReferencePoint:
    tp: int
    fp: int


def build_grid(positives, negatives):
    tp_vals = np.arange(positives + 1)
    fp_vals = np.arange(negatives + 1)
    tp, fp = np.meshgrid(tp_vals, fp_vals, indexing="ij")
    fn = positives - tp
    tn = negatives - fp
    return ConfusionGrid(tp, fp, tn, fn, positives + negatives)


def _safe_div(num, den):
    num_arr = np.asarray(num, dtype=float)
    den_arr = np.asarray(den, dtype=float)
    out = np.zeros_like(num_arr, dtype=float)
    return np.divide(num_arr, den_arr, out=out, where=den_arr != 0)


def accuracy(grid):
    return _safe_div(grid.tp + grid.tn, grid.total)


def precision(grid):
    return _safe_div(grid.tp, grid.tp + grid.fp)


def recall(grid):
    return _safe_div(grid.tp, grid.tp + grid.fn)


def f1_score(prec, rec):
    return _safe_div(2 * prec * rec, prec + rec)


def cohen_kappa(grid):
    po = _safe_div(grid.tp + grid.tn, grid.total)
    pe = _safe_div(
        (grid.tp + grid.fp) * (grid.tp + grid.fn)
        + (grid.fn + grid.tn) * (grid.fp + grid.tn),
        grid.total * grid.total,
    )
    return _safe_div(po - pe, 1 - pe)


def matthews_corr(grid):
    num = grid.tp * grid.tn - grid.fp * grid.fn
    den = np.sqrt(
        (grid.tp + grid.fp)
        * (grid.tp + grid.fn)
        * (grid.tn + grid.fp)
        * (grid.tn + grid.fn)
    )
    return _safe_div(num, den)


def metric_matrices(positives, negatives):
    grid = build_grid(positives, negatives)
    prec = precision(grid)
    rec = recall(grid)
    return {
        "Accuracy": accuracy(grid), "Precision": prec, "TPR (Recall)": rec,
        "F1-Score": f1_score(prec, rec), "Cohen's Kappa": cohen_kappa(grid),
        "MCC": matthews_corr(grid),
    }


def reference_metrics(positives, negatives, ref):
    fn = positives - ref.tp; tn = negatives - ref.fp
    grid = ConfusionGrid(ref.tp, ref.fp, tn, fn, positives + negatives)
    prec = precision(grid); rec = recall(grid)
    return {
        "Accuracy": accuracy(grid), "Precision": prec, "TPR (Recall)": rec,
        "F1-Score": f1_score(prec, rec), "Cohen's Kappa": cohen_kappa(grid),
        "MCC": matthews_corr(grid),
    }