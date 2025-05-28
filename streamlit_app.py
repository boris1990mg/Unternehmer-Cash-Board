import os
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_PORT"] = "10000"
os.environ["STREAMLIT_SERVER_ENABLECORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

import streamlit as st

st.set_page_config(page_title="Finanzanalyse App", layout="centered")
st.title("📊 Finanzanalyse Web-App")
st.markdown("Die App ist erfolgreich gestartet! 🚀")