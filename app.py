import streamlit as st
from src.loader import load_csv
from src.eda import get_column_info, get_missing_values, get_descriptive_stats
from src.charts import numeric_histogram, categorical_bar

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
    st.dataframe(get_column_info(df))

    st.markdown("## Missing Values")
    st.dataframe(get_missing_values(df))

    st.markdown("## Descriptive Statistics")
    st.dataframe(get_descriptive_stats(df))

    st.markdown("## Automatic Charts")

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    if numeric_cols:
        selected_numeric = st.selectbox(
            "Select a numeric column",
            numeric_cols
        )
        st.plotly_chart(
            numeric_histogram(df, selected_numeric),
            use_container_width=True
        )

    if categorical_cols:
        selected_categorical = st.selectbox(
            "Select a categorical column",
            categorical_cols
        )
        st.plotly_chart(
            categorical_bar(df, selected_categorical),
            use_container_width=True
        )

else:
    st.info("Upload a CSV file to begin.")
