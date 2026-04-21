import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="AI Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

# Header principal
st.title("📊 AI Analytics Copilot")
st.subheader("Transform your CSV data into insights with AI")

st.markdown("---")

# Introdução
st.write("""
Upload a CSV file and unlock:

- Executive summaries  
- Automatic charts  
- Forecasting  
- Anomaly detection  
- AI-powered insights
""")

# Upload area
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    st.write("Preview coming soon...")
