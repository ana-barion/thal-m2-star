import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def bin_t2star_ms(t2star_ms: pd.Series) -> pd.Series:
    # Example cardiac T2* bins; adjust per site/protocol
    # Normal > 20, Mild 14-20, Moderate 10-14, Severe < 10
    bins = [-np.inf, 10, 14, 20, np.inf]
    labels = ['severe', 'moderate', 'mild', 'normal']
    return pd.cut(t2star_ms, bins=bins, labels=labels, right=True, include_lowest=True)

def make_splits(df: pd.DataFrame, y_col: str, test_size=0.2, val_size=0.2, random_state=42):
    # Split into train/valid/test with stratification
    train_df, test_df = train_test_split(df, test_size=test_size, stratify=df[y_col], random_state=random_state)
    # Recompute val fraction relative to remaining
    val_rel = val_size / (1 - test_size)
    train_df, val_df = train_test_split(train_df, test_size=val_rel, stratify=train_df[y_col], random_state=random_state)
    return train_df, val_df, test_df

def add_missing_indicators(df: pd.DataFrame, cols):
    for c in cols:
        df[f"{c}__is_missing"] = df[c].isna().astype(int)
    return df