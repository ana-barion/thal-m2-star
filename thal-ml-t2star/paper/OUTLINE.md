# Paper Outline (Draft)

## Title
Predicting Iron Overload Severity in Transfusion-Dependent Thalassemia Using MRI T2* and Routine Labs: A Transparent Machine Learning Study

## Abstract (structured)
- **Background:** Clinical importance of cardiac/hepatic iron; role of T2*.  
- **Objective:** Build interpretable prediction models for severity categories; evaluate clinical utility.
- **Methods:** Dataset, splits, models (logistic, XGBoost), metrics (AUROC, macro-F1, calibration, decision curves).  
- **Results:** Primary performance; calibration; decision-curve summary.  
- **Conclusion:** Potential triage value; limitations and generalizability; future work.

## Introduction
- Burden of iron overload and cardiac risk; T2* as reference standard.
- Clinical decision need (who needs intensified chelation / closer follow-up?).
- Contribution: transparent ML + practical scorecard + DCA.

## Methods
- Data source, inclusion/exclusion; de-identification.  
- Outcomes (bins or continuous); features (T2*, ± labs).  
- Preprocessing; handling missingness; patient-level splits; class imbalance strategy.  
- Models & tuning (nested CV); interpretability (coefficients/SHAP).  
- Metrics & statistics: AUROC, PR, calibration (Brier, reliability), DCA; CIs via bootstrapping.  
- Sensitivity analyses and fairness checks.  
- Reporting: TRIPOD+AI checklist.

## Results
- Cohort characteristics (Table 1).  
- Discrimination & calibration (Table 2, Fig 1–2).  
- DCA (Fig 3): net benefit vs treat-all/none.  
- Ablations and robustness.  
- Scorecard derivation and performance.

## Discussion
- Clinical implications and scenarios.  
- Limitations (single dataset, potential spectrum bias, imaging protocol variability).  
- Next steps: external validation, multi-site collaboration, prospective study.

## Reproducibility
- Data provenance + code availability + environment details.