import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.parser import extract_text_from_pdf
from src.preprocessor import preprocess_text
from src.semantic_matcher import calculate_semantic_match
from src.job_loader import load_jobs
from src.skill_extractor import load_skills, extract_skills


# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("Resume-to-Job Matching NLP System")


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


# ---------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------

if uploaded_file:

    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # ---------------------------------------------------
    # RESUME PARSING
    # ---------------------------------------------------

    resume_text = extract_text_from_pdf(
        "temp_resume.pdf"
    )

    # ---------------------------------------------------
    # PREPROCESSING
    # ---------------------------------------------------

    cleaned_resume = preprocess_text(
        resume_text
    )

    # ---------------------------------------------------
    # LOAD JOBS + SKILLS
    # ---------------------------------------------------

    jobs = load_jobs(
        "data/jobs.txt"
    )

    skills_list = load_skills(
        "data/skills.txt"
    )

    # ---------------------------------------------------
    # EXTRACT RESUME SKILLS
    # ---------------------------------------------------

    resume_skills = extract_skills(
        cleaned_resume,
        skills_list
    )

    # ---------------------------------------------------
    # STORE RESULTS
    # ---------------------------------------------------

    results = []

    # ---------------------------------------------------
    # JOB MATCHING LOOP
    # ---------------------------------------------------

    for job in jobs:

        # Preprocess job text
        cleaned_job = preprocess_text(job)

        # Semantic similarity score
        score = calculate_semantic_match(
            cleaned_resume,
            cleaned_job
        )

        # Extract job title
        title = job.split("\n")[0]

        # Extract job skills
        job_skills = extract_skills(
            cleaned_job,
            skills_list
        )

        # Find missing skills
        missing_skills = []

        for skill in job_skills:

            if skill not in resume_skills:
                missing_skills.append(skill)

        # Store final result
        results.append(
            (
                title,
                score,
                missing_skills
            )
        )

    # ---------------------------------------------------
    # SORT RESULTS
    # ---------------------------------------------------

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # ---------------------------------------------------
    # DISPLAY RESULTS
    # ---------------------------------------------------

    st.subheader("Top Matching Jobs")

    for title, score, missing_skills in results:

        st.write(f"### {title}")

        st.write(
            f"Match Score: {score}%"
        )

        st.write(
            f"Missing Skills: {missing_skills}"
        )

    # ---------------------------------------------------
    # ANALYTICS DATAFRAME
    # ---------------------------------------------------

    df = pd.DataFrame(
        results,
        columns=[
            "Job Title",
            "Match Score",
            "Missing Skills"
        ]
    )

    # ---------------------------------------------------
    # SHOW ANALYTICS TABLE
    # ---------------------------------------------------

    st.subheader("Job Match Analytics")

    st.dataframe(df)

    # ---------------------------------------------------
    # MATCH SCORE VISUALIZATION
    # ---------------------------------------------------

    st.subheader("Match Score Visualization")

    fig, ax = plt.subplots()

    ax.bar(
        df["Job Title"],
        df["Match Score"]
    )

    ax.set_xlabel("Jobs")

    ax.set_ylabel("Match Score")

    ax.set_title(
        "Resume vs Job Match Scores"
    )

    st.pyplot(fig)

    # ---------------------------------------------------
    # RESUME SKILLS DISPLAY
    # ---------------------------------------------------

    st.subheader("Extracted Resume Skills")

    st.write(resume_skills)