import streamlit as st
from resume_parser import extract_text_from_pdf
from job_description_matcher import calculate_similarity
from utils import clean_text, extract_keywords

st.set_page_config(page_title="Manuel AI Resume Matcher", layout="centered")
st.title("Manuel AI Resume Matcher")

jd_text = st.text_area("Paste the Job Description here:")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=['pdf'])

if jd_text and resume_file:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(resume_file)
        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(jd_text)

        score = calculate_similarity(cleaned_resume, cleaned_jd)
        st.success(f"✅ Match Score: {score}%")

        jd_keywords = extract_keywords(jd_text)
        resume_keywords = extract_keywords(resume_text)

        missing_keywords = set(jd_keywords) - set(resume_keywords)
        if missing_keywords:
            st.info("🧩 Consider adding these keywords:")
            st.write(", ".join(missing_keywords))
