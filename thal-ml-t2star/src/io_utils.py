from pathlib import Path
import pandas as pd

def read_labels(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() in {'.xlsx', '.xls'}:
        return pd.read_excel(path)
    return pd.read_csv(path)

def ensure_dirs(*paths: str | Path) -> None:
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)