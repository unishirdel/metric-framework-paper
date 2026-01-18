# Metric Framework Paper Notebooks

## Purpose
- [Add 2-3 sentences describing the paper and what the notebooks reproduce.]

## Paper
- Title: A Framework for Binary Classification Evaluation Metrics
- Authors: Mohammad Shirdel; Mario Di Mauro; Antonio Liotta
- Venue/Year: submitted to Information Sciences, 2025
- Preprint: SSRN 5779321
- DOI: https://doi.org/10.2139/ssrn.5779321

## Repository layout
- notebooks/ : one notebook per figure number
- src/metric_paper/ : reusable metric + plotting code
- scripts/ : command-line entry points
- figures/ : exported plots (PNG/SVG/PDF)
- data/ : generated data notes (no external dataset)

## Setup
- Option A: conda
  - conda env create -f environment.yml
  - conda activate metric-framework-paper
- Option B: pip
  - pip install -r requirements.txt

## Reproducing figures
- [List each figure notebook and the figure it generates.]
- [Note where output files are saved.]

## Metric generator demo
- [Describe expected inputs/outputs.]
- Example: python scripts/run_metric_generator.py --a 1.0 --b 0.0 --variable x

## Citation
- See CITATION.cff

## Acknowledgements
- [Add funding institutions and grant numbers, if applicable.]

## Notes
- [Add any assumptions, random seeds, or version pinning details.]
