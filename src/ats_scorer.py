def calculate_skill_match(
    resume_skills,
    job_skills
):

    if len(job_skills) == 0:
        return 0

    matched_skills = 0

    for skill in job_skills:

        if skill in resume_skills:
            matched_skills += 1

    return round(
        (matched_skills / len(job_skills)) * 100,
        2
    )


def calculate_resume_strength(
    resume_skills
):

    skill_count = len(resume_skills)

    if skill_count >= 10:
        return 90

    elif skill_count >= 7:
        return 75

    elif skill_count >= 5:
        return 60

    else:
        return 40


def calculate_final_score(
    semantic_score,
    skill_score,
    resume_strength
):

    final_score = (
        semantic_score * 0.5 +
        skill_score * 0.3 +
        resume_strength * 0.2
    )

    return round(final_score, 2)