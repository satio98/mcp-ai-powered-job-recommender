import streamlit as st
from src.helper import extract_text_from_pdf, ask_llm
import base64
from src.job_api import fetch_linkedin_jobs
import time

def display_pdf(uploaded_file):

    """
    Display a PDF file that has been uploaded to Streamlit.

    The PDF will be displayed in an iframe, with the width and height set to 700x1000 pixels.

    Parameters
    ----------
    uploaded_file : UploadedFile
        The uploaded PDF file to display.

    Returns
    -------
    None
    """
    # Read file as bytes:
    bytes_data = uploaded_file.getvalue()
    
    # Convert to Base64
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
    
    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    
    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)

def load_streamlit_page():

    st.set_page_config(layout='wide', page_title='AI Powered Job Recommender System')
    st.title('📄AI Powered Job Recommender')

    col1, col2 = st.columns([0.5, 0.5], gap='large')

    with col1:
        st.subheader('Please upload your resume')
        uploaded_file = st.file_uploader('Please upload your resume', type='pdf')

    return col1, col2, uploaded_file

def safe_fetch_linkedin_jobs(keyword, rows=5, retries=3, delay=5):
    """Fetch jobs from LinkedIn safely with retries"""
    for attempt in range(retries):
        try:
            return fetch_linkedin_jobs(keyword, rows=rows)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                st.warning(f"Failed to fetch jobs for '{keyword}': {e}")
                return []

col1, col2, uploaded_file = load_streamlit_page()

if uploaded_file:
    with col2:
        display_pdf(uploaded_file)

    with col1:
        
        with st.spinner('Extracting text from your resume...'):
            extracted_texts = extract_text_from_pdf(uploaded_file)

        with st.spinner("Summarizing your resume..."):
            summary = ask_llm(f"Summarize this resume highlighting the skills, edcucation, and experience: \n\n{extracted_texts}", max_tokens=500)

        with st.spinner("Finding skill Gaps..."):
            gaps = ask_llm(f"Analyze this resume and highlight missing skills, certifications, and experiences needed for better job opportunities: \n\n{extracted_texts}", max_tokens=400)

        with st.spinner("Creating Future Roadmap..."):
            roadmap = ask_llm(f"Based on this resume, suggest a future roadmap to improve this person's career prospects (Skill to learn, certification needed, industry exposure): \n\n{extracted_texts}", max_tokens=400)

        st.markdown("---")
        st.header("🛠️ Skill Gaps & Missing Areas")
        st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.header("🚀 Future Roadmap & Preparation Strategy")
        st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)

        st.success("✅ Analysis Completed Successfully!")

        if st.button('🔎Get Job Recommendations'):
            with st.spinner('Fetching job recommendations...'):
                keywords = ask_llm(
                    f"Based on this resume summary, suggest 4 the best job titles and keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary: {summary}",
                    max_tokens=100
                )

                search_keywords_clean = [k.strip() for k in keywords.replace("\n", "").split(',')]

            st.success(f'Extracted Job Keywords: {search_keywords_clean}')

            all_jobs = []
            placeholder = st.empty()  # for progress updates

            for i, keyword in enumerate(search_keywords_clean, 1):
                placeholder.text(f"Fetching jobs for '{keyword}' ({i}/{len(search_keywords_clean)})...")
                job_list = safe_fetch_linkedin_jobs(keyword, rows=5)  # reduced rows for speed
                all_jobs.extend(job_list)  # merge properly
                time.sleep(1)  # slight delay to avoid connection resets

            placeholder.text("Job fetch completed!")
                

            st.markdown("---")
            st.header("💼 Top LinkedIn Jobs")

            if all_jobs:
                for job in all_jobs:
                    st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                    st.markdown(f"- 📍 {job.get('location')}")
                    st.markdown(f"- 🔗 [View Job]({job.get('link')})")
                    st.markdown("---")
            else:
                st.warning("No LinkedIn jobs found.")



if __name__ == "__main__":
    pass
