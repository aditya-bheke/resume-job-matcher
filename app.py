from src.matcher import calculate_match


with open("data/resume.txt", "r") as file:
    resume_text = file.read()

with open("data/job.txt", "r") as file:
    job_text = file.read()

score = calculate_match(resume_text, job_text)

print(f"Match Score: {score}%")