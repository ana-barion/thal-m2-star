# Thal-ML-T2Star: Predicting Iron Overload Severity from MRI (T2*) ± Labs

This repository is a **dry-lab, fully reproducible** project to build and evaluate models that predict **cardiac/hepatic iron overload severity** in transfusion-dependent thalassemia using **T2*** MRI (and optionally basic labs).

## Quick start
1. Create a virtual environment and install requirements:
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Place the CHMMOTv1 dataset files under `data/raw/` (see `paper/DATA_SOURCES.md` for links and file layout).
3. Open and run the notebooks in order:
   - `notebooks/01_eda.ipynb`
   - `notebooks/02_modeling.ipynb`
4. Figures are saved to `figures/`. Trained models and processed tables go to `data/processed/`.

## Repo layout
```
data/
  raw/         # put raw downloads here (Excel/CSV, images)
  processed/   # clean tables, splits, model-ready files
figures/       # exported plots
notebooks/
  01_eda.ipynb
  02_modeling.ipynb
paper/
  OUTLINE.md
  DATA_SOURCES.md
src/
  __init__.py
  io_utils.py
  preprocessing.py
  metrics.py
  dca.py                # decision curve analysis (net benefit)
  plotting.py
  modeling.py
```

## Endpoints / labels
We use commonly applied cardiac T2* cut-points as **example bins** (you may vary by site):
- **Normal:** > 20 ms
- **Mild:** 14–20 ms
- **Moderate:** 10–14 ms
- **Severe:** < 10 ms

You can switch to **regression** (predict continuous T2*) or multi-task (cardiac + hepatic).

## Reporting & transparency
- Follows **TRIPOD+AI** items.
- Includes **calibration** and **decision curve analysis** (DCA) against simple strategies.
- Produces a compact **scorecard** distilled from a logistic model for interpretability.