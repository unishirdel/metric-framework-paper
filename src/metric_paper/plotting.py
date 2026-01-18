from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


@dataclass(frozen=True)
class PlotTicks:
    positions: np.ndarray
    labels: list


@dataclass(frozen=True)
class CurveGrid:
    tpr: np.ndarray
    fpr: np.ndarray


def set_plot_style():
    styles = {
        "font.size": 16, "axes.titlesize": 18, "axes.labelsize": 16,
        "xtick.labelsize": 14, "ytick.labelsize": 14, "legend.fontsize": 14,
    }
    plt.rcParams.update(styles)


def build_ticks(max_value, steps):
    positions = np.linspace(0, max_value, steps, dtype=int)
    labels = [f"{x / max_value:.2f}" for x in positions]
    return PlotTicks(positions, labels)


def build_curve_grid(positives, negatives):
    tpr_vals = np.arange(positives + 1) / positives
    fpr_vals = np.arange(negatives + 1) / negatives
    tpr, fpr = np.meshgrid(tpr_vals, fpr_vals, indexing="ij")
    return CurveGrid(tpr, fpr)


def _heatmap_ax(matrix):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(matrix, cmap="viridis", cbar=True, ax=ax)
    return ax


def _apply_ticks(ax, ticks):
    ax.set_xticks(ticks.positions + 0.5)
    ax.set_xticklabels(ticks.labels)
    ax.set_yticks(ticks.positions + 0.5)
    ax.set_yticklabels(ticks.labels)
    ax.invert_yaxis()


def _apply_labels(title):
    plt.xlabel("FPR (False Positive Rate)")
    plt.ylabel("TPR (True Positive Rate)")
    plt.title(title)
    plt.gca().set_aspect("equal", adjustable="box")


def _fill_for_contour(matrix):
    finite = np.isfinite(matrix)
    floor = np.nanmin(matrix[finite]) if finite.any() else 0
    return np.nan_to_num(matrix, nan=floor - 1)


def _iso_contours(matrix, ref_value, grid):
    filled = _fill_for_contour(matrix)
    low = np.min(filled)
    plt.contourf(grid.fpr, grid.tpr, filled, levels=[low, ref_value], colors="red", alpha=0.3)
    cs = plt.contour(grid.fpr, grid.tpr, filled, levels=[ref_value], colors="red", linewidths=2)
    plt.clabel(cs, inline=True, fontsize=14, fmt="%.3f")


def _iso_axes(title):
    plt.xlabel("FPR (False Positive Rate)")
    plt.ylabel("TPR (True Positive Rate)")
    plt.title(title)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.tight_layout()


class HeatmapPlotter:
    def __init__(self, ticks, title):
        self.ticks = ticks
        self.title = title

    def plot_all(self, matrices):
        for matrix in matrices.values():
            self._plot(matrix)

    def _plot(self, matrix):
        ax = _heatmap_ax(matrix)
        _apply_ticks(ax, self.ticks)
        _apply_labels(self.title)
        plt.show()


class IsoCurvePlotter:
    def __init__(self, grid, title):
        self.grid = grid
        self.title = title

    def plot_all(self, matrices, ref_values):
        for name, matrix in matrices.items():
            self._plot(matrix, ref_values[name])

    def _plot(self, matrix, ref_value):
        value = float(ref_value)
        plt.figure(figsize=(6, 6))
        _iso_contours(matrix, value, self.grid)
        _iso_axes(self.title)
        plt.show()