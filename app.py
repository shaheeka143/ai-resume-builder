from flask import Flask, render_template, request
from nlp.keyword_extractor import extract_keywords
from nlp.similarity import compute_similarity
from models.ats_scorer import compute_ats_score
from resume.pdf_generator import generate_pdf
from resume.docx_generator import generate_docx

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # ---------- COLLECT FORM DATA ----------
        student = {
            "name": request.form.get("name", ""),
            "email": request.form.get("email", ""),
            "phone": request.form.get("phone", ""),
            "linkedin": request.form.get("linkedin", ""),
            "summary": request.form.get("summary", ""),

            # Clean skills list
            "skills": [
                s.strip()
                for s in request.form.get("skills", "").split(",")
                if s.strip()
            ],

            # Clean education list
            "education": [
                e.strip()
                for e in request.form.get("education", "").split("\n")
                if e.strip()
            ],

            # Clean projects list
            "projects": [
                p.strip()
                for p in request.form.get("projects", "").split("\n")
                if p.strip()
            ],

            # Clean certifications list
            "certifications": [
                c.strip()
                for c in request.form.get("certifications", "").split(",")
                if c.strip()
            ],

            "declaration": request.form.get("declaration", "")
        }

        role = request.form.get("role", "AI Engineer")
        template = request.form.get("template", "professional")

        # ---------- ATS SCORING ----------
        job_desc = f"We are hiring a {role} with strong technical skills."

        keywords = extract_keywords(job_desc)
        similarity = compute_similarity(student, job_desc)
        score, feedback = compute_ats_score(student, keywords, similarity)

        # ---------- GENERATE FILES ----------
        pdf_path = generate_pdf(student, role, template)
        docx_path = generate_docx(student, role, template)

        return render_template(
            "result.html",
            score=score,
            feedback=feedback,
            pdf_path=pdf_path,
            docx_path=docx_path,
            role=role,
            student=student
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

