def recommend_jobs(skills):
    job_roles = {
        "Data Scientist": ["python", "machine learning", "data science"],
        "Web Developer": ["html", "css", "javascript"],
        "Backend Developer": ["node", "sql"],
        "AI Engineer": ["python", "deep learning"]
    }

    matched_jobs = []

    for job, req_skills in job_roles.items():
        if any(skill in skills for skill in req_skills):
            matched_jobs.append(job)

    return matched_jobs


def suggest_skills(user_skills, job_desc):
    suggestions = []

    job_keywords = job_desc.lower().split()

    for word in job_keywords:
        if word not in user_skills:
            suggestions.append(word)

    return list(set(suggestions))[:10]
