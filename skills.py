def extract_skills(text):
    skill_list = [
        "python", "java", "c++", "machine learning",
        "data science", "sql", "html", "css",
        "javascript", "react", "node", "deep learning"
    ]

    found_skills = []

    for skill in skill_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
