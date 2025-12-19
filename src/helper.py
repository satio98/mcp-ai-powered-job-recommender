import fitz
import os
from dotenv import load_dotenv

def extract_text_from_pdf(uploaded_file):

    doc = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    text = ''

    for page in doc:
        text += page.get_text()

    return text 

if __name__ == '__main__':
    pdf_path = 'pdf\CV-Laksamana Satio Syailendra.pdf'
    print(extract_text_from_pdf(pdf_path))