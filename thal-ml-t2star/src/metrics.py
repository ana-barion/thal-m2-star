import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, f1_score, brier_score_loss
from sklearn.calibration import calibration_curve

def compute_metrics(y_true, y_prob, y_pred, average='macro'):
    return {
        'auroc': roc_auc_score(y_true, y_prob, multi_class='ovr' if len(np.unique(y_true))>2 else 'raise'),
        'macro_f1': f1_score(y_true, y_pred, average=average),
        'brier': brier_score_loss(y_true, y_prob) if len(np.unique(y_true))==2 else np.nan
    }

def reliability_curve(y_true, y_prob, n_bins=10):
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy='uniform')
    return pd.DataFrame({'prob_pred': prob_pred, 'prob_true': prob_true})