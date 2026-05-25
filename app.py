# Import PDF parser
from src.parser import extract_text_from_pdf

# Import preprocessing pipeline
from src.preprocessor import preprocess_text

# Import similarity calculator
from src.semantic_matcher import calculate_semantic_match

# Import multi-job loader
from src.job_loader import load_jobs

# Import skill extraction functions
from src.skill_extractor import load_skills, extract_skills


# Extract raw text from resume PDF
resume_text = extract_text_from_pdf("data/resume.pdf")

# Clean and normalize resume text
cleaned_resume = preprocess_text(resume_text)

# Load all job descriptions
jobs = load_jobs("data/jobs.txt")

# Load master skills database
skills_list = load_skills("data/skills.txt")

# Extract skills from resume
resume_skills = extract_skills(cleaned_resume, skills_list)

# Store all job matching results
results = []

# Loop through every job
for job in jobs:

    # Clean job description text
    cleaned_job = preprocess_text(job)

    # Calculate similarity between resume and job
    score = calculate_semantic_match(cleaned_resume, cleaned_job)

    # Extract first line as job title
    title = job.split("\n")[0]

    # Extract skills from current job
    job_skills = extract_skills(cleaned_job, skills_list)

    # Store missing skills
    missing_skills = []

    # Check which job skills are absent in resume
    for skill in job_skills:

        # If resume lacks required skill
        if skill not in resume_skills:

            # Add skill to missing list
            missing_skills.append(skill)

    # Store title, score, and missing skills
    results.append((title, score, missing_skills))


# Sort jobs by highest similarity score
results.sort(key=lambda x: x[1], reverse=True)

# Print final ranked jobs
print("\nTop Matching Jobs:\n")

# Display all recommendations
for title, score, missing_skills in results:

    print(f"{title} → {score}%")

    print(f"Missing Skills: {missing_skills}\n")