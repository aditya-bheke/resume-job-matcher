from src.parser import extract_text_from_pdf
from src.preprocessor import preprocess_text
from src.matcher import calculate_match
from src.job_loader import load_jobs


resume_text = extract_text_from_pdf("data/resume.pdf")

cleaned_resume = preprocess_text(resume_text)

jobs = load_jobs("data/jobs.txt")

results = []

for job in jobs:
    cleaned_job = preprocess_text(job)

    score = calculate_match(cleaned_resume, cleaned_job)

    results.append((job.split("\n")[0], score))


results.sort(key=lambda x: x[1], reverse=True)

print("\nTop Matching Jobs:\n")

for title, score in results:
    print(f"{title} → {score}%")