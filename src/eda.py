import pandas as pd


def get_column_info(df: pd.DataFrame) -> pd.DataFrame:
    column_info = df.dtypes.astype(str).reset_index()
    column_info.columns = ["column", "dtype"]
    return column_info


def get_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["column", "missing_values"]
    missing_df["missing_pct"] = (missing_df["missing_values"] / len(df) * 100).round(2)
    return missing_df.sort_values(by="missing_values", ascending=False)


def get_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include="all").transpose()
