import numpy as np
import pandas as pd

def net_benefit(y_true, y_prob, threshold):
    # y_true: binary {0,1}, y_prob: predicted probability for class 1
    # Net benefit = (TP/N) - (FP/N) * (pt / (1-pt))
    pt = threshold
    y_pred = (y_prob >= pt).astype(int)
    N = len(y_true)
    TP = ((y_pred == 1) & (y_true == 1)).sum()
    FP = ((y_pred == 1) & (y_true == 0)).sum()
    return (TP / N) - (FP / N) * (pt / (1 - pt + 1e-12))

def decision_curve(y_true, y_prob, thresholds=None):
    if thresholds is None:
        thresholds = np.linspace(0.01, 0.99, 99)
    data = []
    y_true = np.asarray(y_true).astype(int)
    y_prob = np.asarray(y_prob)
    prevalence = y_true.mean()
    for t in thresholds:
        nb_model = net_benefit(y_true, y_prob, t)
        # Treat-all strategy net benefit = prevalence - (1-prevalence)*(t/(1-t))
        nb_all = prevalence - (1 - prevalence) * (t / (1 - t + 1e-12))
        # Treat-none strategy = 0
        data.append({'threshold': t, 'nb_model': nb_model, 'nb_all': nb_all, 'nb_none': 0.0})
    return pd.DataFrame(data)