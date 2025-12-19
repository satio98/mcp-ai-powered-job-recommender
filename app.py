import streamlit as st
from src.helper import extract_text_from_pdf

uploaded_file = st.file_uploader('Upload', type = 'pdf')

if uploaded_file:
    st.markdown(extract_text_from_pdf(uploaded_file))

if __name__ == "__main__":
    pass
