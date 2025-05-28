import streamlit as st

st.set_page_config(page_title="Finanzanalyse-App", layout="wide")
st.title("📊 Finanzanalyse-Tool für BWA-Daten")
st.markdown("Diese App dient als Ausgangspunkt für den Upload und die Analyse deiner BWA-Dateien. Weitere Funktionen folgen.")
uploaded_file = st.file_uploader("Lade hier deine BWA-Datei hoch (PDF, Excel, CSV)", type=["pdf", "xlsx", "csv"])
if uploaded_file:
    st.success(f"Datei erfolgreich hochgeladen: {uploaded_file.name}")
