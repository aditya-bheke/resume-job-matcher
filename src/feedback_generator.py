def generate_feedback(
    resume_skills,
    missing_skills
):

    feedback = []

    # Remove duplicates
    unique_missing_skills = list(
        set(missing_skills)
    )

    # Generate recommendations
    for skill in unique_missing_skills:

        feedback.append(
            f"Consider learning or adding '{skill}' to your resume."
        )

    # Resume strength feedback
    if len(resume_skills) >= 10:

        feedback.append(
            "Your resume shows strong technical skill diversity."
        )

    elif len(resume_skills) >= 5:

        feedback.append(
            "Your resume has moderate technical coverage."
        )

    else:

        feedback.append(
            "Your resume may need more technical skills/projects."
        )

    return feedback