def extract_resume_sections(text):

    # Common resume section headers
    section_keywords = [
        "education",
        "skills",
        "projects",
        "experience",
        "certifications",
        "internship",
        "achievements"
    ]

    # Store extracted sections
    sections = {}

    # Split resume into lines
    lines = text.split("\n")

    current_section = "other"

    sections[current_section] = []

    # Process every line
    for line in lines:

        clean_line = line.strip().lower()

        # Check if line is section heading
        matched_section = None

        for keyword in section_keywords:

            if keyword in clean_line:

                matched_section = keyword
                break

        # If new section found
        if matched_section:

            current_section = matched_section

            if current_section not in sections:
                sections[current_section] = []

        else:

            # Store content inside current section
            sections[current_section].append(
                line.strip()
            )

    return sections