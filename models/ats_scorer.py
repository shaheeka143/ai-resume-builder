def compute_ats_score(student, keywords, similarity):
    skills = " ".join(student["skills"]).lower()

    keyword_matches = sum(1 for k in keywords if k in skills)
    keyword_score = (keyword_matches / len(keywords)) * 100 if keywords else 0

    completeness = 0
    sections = ["skills", "education", "projects", "certifications"]
    for sec in sections:
        if student.get(sec):
            completeness += 25

    final_score = round(
        0.4 * keyword_score +
        0.4 * similarity +
        0.2 * completeness
    )

    feedback = []
    if keyword_score < 50:
        feedback.append("Add more job-specific keywords.")
    if similarity < 50:
        feedback.append("Improve project relevance.")
    if completeness < 75:
        feedback.append("Complete all resume sections.")

    return final_score, feedback
