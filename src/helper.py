import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI
from apify_client import ApifyClient

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_text_from_pdf(uploaded_file):

    doc = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    text = ''

    for page in doc:
        text += page.get_text()

    return text 

def ask_llm(prompt, max_tokens = 500):

    response = client.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            {
                'role' : 'user',
                'content' : prompt
            }
        ],
        temperature = 0.5,
        max_tokens = max_tokens
    )

    return response.choices[0].message.content

if __name__ == '__main__':
    pdf_path = 'pdf\CV-Laksamana Satio Syailendra.pdf'
    print(extract_text_from_pdf(pdf_path))