from src.parser import extract_text_from_pdf
from src.matcher import calculate_match


resume_text = extract_text_from_pdf("data/resume.pdf")

with open("data/job.txt", "r") as file:
    job_text = file.read()

score = calculate_match(resume_text, job_text)

print("\nExtracted Resume Text:\n")
print(resume_text)

print(f"\nMatch Score: {score}%")