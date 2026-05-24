from src.parser import extract_text_from_pdf
from src.matcher import calculate_match
from src.preprocessor import preprocess_text


resume_text = extract_text_from_pdf("data/resume.pdf")

with open("data/job.txt", "r") as file:
    job_text = file.read()

cleaned_resume = preprocess_text(resume_text)
cleaned_job = preprocess_text(job_text)

score = calculate_match(cleaned_resume, cleaned_job)

print("\nCleaned Resume Text:\n")
print(cleaned_resume)

print(f"\nMatch Score: {score}%")