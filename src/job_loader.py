def load_jobs(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    jobs = content.split("===")

    cleaned_jobs = []

    for job in jobs:
        cleaned_jobs.append(job.strip())

    return cleaned_jobs