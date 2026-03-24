import streamlit as st
from parser import parse_pdf, parse_docx
from skills import extract_skills
from recommender import recommend_jobs, suggest_skills
from fake_detector import detect_fake_skills

st.title("AI Resume Screening System")

job_desc = st.text_area("Enter Job Description")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if st.button("Analyze Resume"):
    if uploaded_file is not None:

        if uploaded_file.name.endswith(".pdf"):
            text = parse_pdf(uploaded_file)
        else:
            text = parse_docx(uploaded_file)

        skills = extract_skills(text)
        jobs = recommend_jobs(skills)
        missing_skills = suggest_skills(skills, job_desc)
        fake_skills = detect_fake_skills(text, skills)

        st.subheader("Extracted Skills")
        st.write(skills)

        st.subheader("Recommended Jobs")
        st.write(jobs)

        st.subheader("Skills to Improve")
        st.write(missing_skills)

        st.subheader("Fake Skills Detected")
        st.write(fake_skills)

    else:
        st.warning("Please upload a resume")
