# Data Sources & Layout

## Primary dataset
- **CHMMOTv1** (Cardiac & Hepatic Multi-Echo T2* MRI in thalassemia). Download and place files as follows:

```
data/raw/
  CHMMOTv1_labels.xlsx        # patient-level table with T2*/R2*, severity, labs
  cardiac_images/…            # optional: image files if downloaded
  hepatic_images/…
```

> Note: If you only have the Excel/CSV labels, you can run the **tabular** pipeline (skip image processing).

## Processed exports (created by notebooks)
```
data/processed/
  cohort_clean.parquet
  split_train.parquet
  split_valid.parquet
  split_test.parquet
  model_logreg.joblib
  model_xgb.json
```