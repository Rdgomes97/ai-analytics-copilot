import pandas as pd

def load_csv(uploaded_file):
    """
    Reads uploaded CSV file safely.
    """

    try:
        df = pd.read_csv(uploaded_file)
        return df

    except Exception:
        df = pd.read_csv(uploaded_file, encoding="latin1")
        return df
