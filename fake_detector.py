def detect_fake_skills(text, skills):
    fake_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            if "project" not in text.lower() and "experience" not in text.lower():
                fake_skills.append(skill)

    return fake_skills
