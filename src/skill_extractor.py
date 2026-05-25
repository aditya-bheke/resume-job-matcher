# Function to load all skills from skills.txt
def load_skills(file_path):

    # Open skills file
    with open(file_path, "r") as file:

        # Read skills line-by-line
        skills = file.read().splitlines()

    # Convert every skill into lowercase
    # Ensures consistent matching
    return [skill.lower() for skill in skills]


# Function to detect skills inside text
def extract_skills(text, skills_list):

    # Store detected skills
    extracted_skills = []

    # Convert text to lowercase
    text = text.lower()

    # Check every known skill
    for skill in skills_list:

        # If skill exists in text
        if skill in text:

            # Add skill to extracted list
            extracted_skills.append(skill)

    # Return detected skills
    return extracted_skills