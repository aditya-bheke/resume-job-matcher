# Function to load multiple jobs from jobs.txt
def load_jobs(file_path):

    # Open jobs file
    with open(file_path, "r") as file:

        # Read entire file content
        content = file.read()

    # Split jobs using === separator
    jobs = content.split("===")

    # Store cleaned jobs
    cleaned_jobs = []

    # Loop through every job
    for job in jobs:

        # Remove extra spaces/newlines
        cleaned_jobs.append(job.strip())

    # Return final list of jobs
    return cleaned_jobs