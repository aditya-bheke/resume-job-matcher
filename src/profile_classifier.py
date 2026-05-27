def classify_profile(resume_skills):

    profile_keywords = {

        "AI/ML Engineer": [
            "python",
            "tensorflow",
            "pytorch",
            "machine learning",
            "deep learning",
            "nlp",
            "computer vision"
        ],

        "Data Analyst": [
            "sql",
            "excel",
            "power bi",
            "tableau",
            "statistics",
            "data analysis"
        ],

        "Web Developer": [
            "html",
            "css",
            "javascript",
            "react",
            "nodejs",
            "mongodb"
        ],

        "Backend Developer": [
            "java",
            "spring",
            "mysql",
            "api",
            "backend",
            "django",
            "flask"
        ],

        "Cloud/DevOps Engineer": [
            "aws",
            "docker",
            "kubernetes",
            "ci/cd",
            "linux",
            "terraform"
        ]
    }

    profile_scores = {}

    # Count matching skills
    for profile, keywords in profile_keywords.items():

        score = 0

        for skill in keywords:

            if skill in resume_skills:
                score += 1

        profile_scores[profile] = score

    # Find highest matching profile
    best_profile = max(
        profile_scores,
        key=profile_scores.get
    )

    return best_profile, profile_scores