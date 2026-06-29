"""Simple data analysis utilities.

Usage:
  - Run as a script to load a CSV and print basic stats:
      python simple_analysis.py data.csv

Provides:
  - load_csv(path): returns pandas.DataFrame
  - summarize(df): prints row/column counts and numeric column statistics
  - save_summary(df, out_path): saves summary as CSV
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    numeric = df.select_dtypes(include="number")
    desc = numeric.describe().T
    desc = desc[["count", "mean", "std", "min", "25%", "50%", "75%", "max"]]
    meta = {
        "rows": len(df),
        "columns": len(df.columns),
        "numeric_columns": numeric.shape[1],
    }
    print(f"Rows: {meta['rows']}, Columns: {meta['columns']}, Numeric columns: {meta['numeric_columns']}")
    print(desc)
    return desc


def save_summary(df: pd.DataFrame, out_path: str | Path) -> None:
    out = Path(out_path)
    df.to_csv(out)
    print(f"Saved summary to {out}")


def main(argv: Optional[list[str]] = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python simple_analysis.py <data.csv> [summary_out.csv]")
        return 1
    data_path = argv[0]
    out_path = argv[1] if len(argv) > 1 else "summary.csv"

    df = load_csv(data_path)
    summary = summarize(df)
    save_summary(summary, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
