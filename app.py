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

# Se arquivo enviado
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

else:
    st.info("Upload a CSV file to begin.")
