import streamlit as st
from src.loader import load_csv

# Configuração da página
st.set_page_config(
    page_title="AI Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 AI Analytics Copilot")
st.subheader("Transform your CSV data into insights with AI")

st.markdown("---")

# Upload
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = load_csv(uploaded_file)

    st.success("File uploaded successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.markdown("## Data Preview")
    st.dataframe(df.head())

    st.markdown("## Column Information")
    column_info = df.dtypes.astype(str).reset_index()
    column_info.columns = ["column", "dtype"]
    st.dataframe(column_info)

    st.markdown("## Missing Values")
    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["column", "missing_values"]
    missing_df["missing_pct"] = (missing_df["missing_values"] / len(df) * 100).round(2)
    st.dataframe(missing_df.sort_values(by="missing_values", ascending=False))

    st.markdown("## Descriptive Statistics")
    st.dataframe(df.describe(include="all").transpose())

else:
    st.info("Upload a CSV file to begin.")
