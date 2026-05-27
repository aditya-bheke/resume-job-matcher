import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.parser import extract_text_from_pdf
from src.preprocessor import preprocess_text

from src.job_loader import load_jobs

from src.skill_extractor import (
    load_skills,
    extract_skills
)

from src.feedback_generator import (
    generate_feedback
)

from src.ats_scorer import (
    calculate_skill_match,
    calculate_resume_strength,
    calculate_final_score
)

from src.section_extractor import (
    extract_resume_sections
)

from src.profile_classifier import (
    classify_profile
)

from src.vector_store import (
    create_job_embeddings,
    retrieve_top_jobs
)


# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title("Resume-to-Job Matching NLP System")


# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


# ---------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------

if uploaded_file:

    # ---------------------------------------------------
    # SAVE TEMP PDF
    # ---------------------------------------------------

    with open("temp_resume.pdf", "wb") as f:

        f.write(uploaded_file.read())

    # ---------------------------------------------------
    # EXTRACT RESUME TEXT
    # ---------------------------------------------------

    resume_text = extract_text_from_pdf(
        "temp_resume.pdf"
    )

    # ---------------------------------------------------
    # EXTRACT RESUME SECTIONS
    # ---------------------------------------------------

    resume_sections = extract_resume_sections(
        resume_text
    )

    # ---------------------------------------------------
    # PREPROCESS RESUME
    # ---------------------------------------------------

    cleaned_resume = preprocess_text(
        resume_text
    )

    # ---------------------------------------------------
    # LOAD JOBS
    # ---------------------------------------------------

    jobs = load_jobs(
        "data/jobs.txt"
    )

    # ---------------------------------------------------
    # CREATE JOB EMBEDDINGS
    # ---------------------------------------------------

    job_embeddings = create_job_embeddings(
        jobs
    )

    # ---------------------------------------------------
    # RETRIEVE TOP JOBS
    # ---------------------------------------------------

    top_jobs = retrieve_top_jobs(
        cleaned_resume,
        jobs,
        job_embeddings,
        top_k=5
    )

    # ---------------------------------------------------
    # LOAD SKILLS DATABASE
    # ---------------------------------------------------

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
    # CLASSIFY CANDIDATE PROFILE
    # ---------------------------------------------------

    predicted_profile, profile_scores = classify_profile(
        resume_skills
    )

    # ---------------------------------------------------
    # CALCULATE RESUME STRENGTH
    # ---------------------------------------------------

    resume_strength = calculate_resume_strength(
        resume_skills
    )

    # ---------------------------------------------------
    # STORE RESULTS
    # ---------------------------------------------------

    results = []

    all_missing_skills = []

    # ---------------------------------------------------
    # PROCESS RETRIEVED JOBS
    # ---------------------------------------------------

    for job, semantic_score in top_jobs:

        # ---------------------------------------------
        # PREPROCESS JOB
        # ---------------------------------------------

        cleaned_job = preprocess_text(
            job
        )

        # ---------------------------------------------
        # EXTRACT JOB TITLE
        # ---------------------------------------------

        title = job.split("\n")[0]

        # ---------------------------------------------
        # EXTRACT JOB SKILLS
        # ---------------------------------------------

        job_skills = extract_skills(
            cleaned_job,
            skills_list
        )

        # ---------------------------------------------
        # CALCULATE SKILL MATCH
        # ---------------------------------------------

        skill_score = calculate_skill_match(
            resume_skills,
            job_skills
        )

        # ---------------------------------------------
        # FIND MISSING SKILLS
        # ---------------------------------------------

        missing_skills = []

        for skill in job_skills:

            if skill not in resume_skills:

                missing_skills.append(skill)

        # ---------------------------------------------
        # STORE GLOBAL MISSING SKILLS
        # ---------------------------------------------

        all_missing_skills.extend(
            missing_skills
        )

        # ---------------------------------------------
        # FINAL ATS SCORE
        # ---------------------------------------------

        final_score = calculate_final_score(
            semantic_score,
            skill_score,
            resume_strength
        )

        # ---------------------------------------------
        # STORE RESULTS
        # ---------------------------------------------

        results.append(
            (
                title,
                semantic_score,
                skill_score,
                resume_strength,
                final_score,
                missing_skills
            )
        )

    # ---------------------------------------------------
    # SORT RESULTS
    # ---------------------------------------------------

    results.sort(
        key=lambda x: x[4],
        reverse=True
    )

    # ---------------------------------------------------
    # DISPLAY CANDIDATE PROFILE
    # ---------------------------------------------------

    st.subheader("Detected Candidate Profile")

    st.write(f"### {predicted_profile}")

    st.write("Profile Matching Scores")

    st.write(profile_scores)

    # ---------------------------------------------------
    # DISPLAY RETRIEVAL RESULTS
    # ---------------------------------------------------

    st.subheader("Semantic Retrieval Results")

    for (
        title,
        semantic_score,
        skill_score,
        resume_strength,
        final_score,
        missing_skills
    ) in results:

        st.write(f"### {title}")

        st.write(
            f"Semantic Similarity: {semantic_score}%"
        )

        st.write(
            f"Skill Match: {skill_score}%"
        )

        st.write(
            f"Resume Strength: {resume_strength}%"
        )

        st.write(
            f"Final ATS Score: {final_score}%"
        )

        st.write(
            f"Missing Skills: {missing_skills}"
        )

    # ---------------------------------------------------
    # CREATE ANALYTICS DATAFRAME
    # ---------------------------------------------------

    df = pd.DataFrame(
        results,
        columns=[
            "Job Title",
            "Semantic Score",
            "Skill Match",
            "Resume Strength",
            "Final ATS Score",
            "Missing Skills"
        ]
    )

    # ---------------------------------------------------
    # DISPLAY ANALYTICS TABLE
    # ---------------------------------------------------

    st.subheader("Job Match Analytics")

    st.dataframe(df)

    # ---------------------------------------------------
    # ATS SCORE VISUALIZATION
    # ---------------------------------------------------

    st.subheader("ATS Score Visualization")

    fig, ax = plt.subplots()

    ax.bar(
        df["Job Title"],
        df["Final ATS Score"]
    )

    ax.set_xlabel("Jobs")

    ax.set_ylabel("ATS Score")

    ax.set_title(
        "Resume vs Job ATS Scores"
    )

    st.pyplot(fig)

    # ---------------------------------------------------
    # DISPLAY RESUME SKILLS
    # ---------------------------------------------------

    st.subheader("Extracted Resume Skills")

    st.write(resume_skills)

    # ---------------------------------------------------
    # DISPLAY RESUME SECTIONS
    # ---------------------------------------------------

    st.subheader("Detected Resume Sections")

    for section, content in resume_sections.items():

        st.write(f"### {section.title()}")

        for line in content:

            if line:

                st.write(f"- {line}")

    # ---------------------------------------------------
    # GENERATE FEEDBACK
    # ---------------------------------------------------

    feedback = generate_feedback(
        resume_skills,
        all_missing_skills
    )

    # ---------------------------------------------------
    # DISPLAY FEEDBACK
    # ---------------------------------------------------

    st.subheader(
        "Resume Improvement Suggestions"
    )

    for item in feedback:

        st.write(f"- {item}")