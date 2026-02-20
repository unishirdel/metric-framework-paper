# Metric Framework Paper Notebooks

## Purpose
This repository provides notebooks and scripts to reproduce figures from the paper and to generate a **single reward-matrix based metric** ($\eta$) symbolically from user-defined coefficients.

## Paper
- Title: A Framework for Binary Classification Evaluation Metrics
- Authors: Mohammad Shirdel; Mario Di Mauro; Antonio Liotta
- Venue/Year: submitted to Information Sciences, 2025
- Preprint: SSRN 5779321
- DOI: https://doi.org/10.2139/ssrn.5779321

## Repository layout
- `notebooks/` : figure notebooks
- `src/metric_paper/` : reusable code (metrics, plotting, metric generator)
- `scripts/` : command-line demo
- `figures/` : generated outputs (SVG)
- `data/` : notes (no external dataset)

## Setup
### Option A: conda
```
conda env create -f environment.yml
conda activate metric-framework-paper
```

### Option B: pip
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## How to run the notebooks
> All notebooks expect the repo root as the working directory.

### Notebook 1 - Iso-curve panels (Figure 1)
**File:** `notebooks/01_fig1_isocurves.ipynb`

**What it does**
- Generates all iso-curve plots for the metrics: Accuracy, Precision, Recall, F1, Cohen's Kappa, MCC.
- Saves each plot to `figures/` as SVG.

**Inputs**
- `positives`, `negatives`: total positives/negatives for the confusion-matrix grid
- `reference = (TP, FP)` reference point used to compute the iso-curve

**Outputs**
- `figures/fig1_isocurve_accuracy.svg`
- `figures/fig1_isocurve_precision.svg`
- `figures/fig1_isocurve_tpr_recall.svg`
- `figures/fig1_isocurve_f1-score.svg`
- `figures/fig1_isocurve_cohens_kappa.svg`
- `figures/fig1_isocurve_mcc.svg`

### Notebook 2 - ROI panels (Figure 2)
**File:** `notebooks/02_fig2_roi.ipynb`

**What it does**
- Plots ROI-based curves: loss probability, expected ROI, worst-case ROI.
- Saves each plot to `figures/` as SVG.

**Inputs**
- `L`, `U`: lower/upper bounds for $ipv_{act}$ (Uniform distribution)
- $\eta$: range of eta values used on the x-axis

**Outputs**
- `figures/fig2_roi_p_loss.svg`
- `figures/fig2_roi_expected.svg`
- `figures/fig2_roi_worst.svg`

### Notebook 3 - Metric generator demo
**File:** `notebooks/03_metric_generator_demo.ipynb`

**What it does**
- Generates a symbolic **metric ($\eta$) equation** from the reward-matrix coefficients.

**Inputs**
- $theta = [\theta_1, \theta_2, \theta_3, \theta_4]$ for the **value** terms of **[TP, FN, FP, TN]**
- $lambda = [\lambda_1, \lambda_2, \lambda_3, \lambda_4]$ for the **investment** terms of **[TP, FN, FP, TN]**

**Output**
- A symbolic equation: `eta = (...)/(...)` (simplified fraction)

## Command-line demo
**File:** `scripts/run_metric_generator.py`

Run:
```
python scripts/run_metric_generator.py
```

It will prompt you for the coefficient lists and output:
```
eta = ( ... )/( ... )
```

You can also pass values directly:
```
python scripts/run_metric_generator.py --theta 1 0 0 1 --lambda 1 1 1 1
```

## Citation
See `CITATION.cff`.

## Acknowledgements
