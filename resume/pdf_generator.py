from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# ---------- TEXT WRAP FUNCTION ----------
def draw_paragraph(c, text, x, y, page_width, line_height=14):
    max_width = page_width - 80
    words = text.split()
    line = ""

    for word in words:
        test_line = line + word + " "
        if c.stringWidth(test_line, "Helvetica", 10) <= max_width:
            line = test_line
        else:
            c.drawString(x, y, line.strip())
            y -= line_height
            line = word + " "

    if line:
        c.drawString(x, y, line.strip())
        y -= line_height

    return y


# ---------- PAGE BREAK HANDLER ----------
def check_page_space(c, y, margin=60):
    if y < margin:
        c.showPage()
        c.setFont("Helvetica", 10)
        return 750
    return y


# ---------- MAIN PDF GENERATOR ----------
def generate_pdf(student, role, template="professional"):
    filename = f"static/{student['name']}_{role}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 60

    # ---------- HEADER ----------
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, y, student["name"])
    y -= 20

    c.setFont("Helvetica", 10)
    contact = f"{student['email']} | {student['phone']}"
    if student.get("linkedin"):
        contact += f" | {student['linkedin']}"
    c.drawCentredString(width / 2, y, contact)
    y -= 25

    # ---------- SECTION HELPER ----------
    def section(title):
        nonlocal y
        y = check_page_space(c, y)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, title.upper())
        y -= 10
        c.line(40, y, width - 40, y)
        y -= 15
        c.setFont("Helvetica", 10)

    # ---------- SUMMARY ----------
    if student.get("summary"):
        section("Summary")
        y = draw_paragraph(c, student["summary"], 40, y, width)
        y -= 5

    # ---------- SKILLS ----------
    if student.get("skills"):
        section("Skills")
        for skill in student["skills"]:
            y = check_page_space(c, y)
            c.setFont("Helvetica", 10)
            c.drawString(40, y, f"• {skill}")
            y -= 15
        y -= 5

    # ---------- EDUCATION ----------
    if student.get("education"):
        section("Education")
        for edu in student["education"]:
            y = check_page_space(c, y)
            y = draw_paragraph(c, edu, 40, y, width)
            y -= 5

    # ---------- PROJECTS (CLEAN VERSION) ----------
    if student.get("projects"):
        section("Projects")

        for proj in student["projects"]:
            y = check_page_space(c, y)

            if "|" in proj:
                title, desc = proj.split("|", 1)
            else:
                title, desc = proj, ""

            # Title in bold
            c.setFont("Helvetica-Bold", 11)
            c.drawString(40, y, title.strip())
            y -= 14

            # Description in normal text
            if desc:
                c.setFont("Helvetica", 10)
                y = draw_paragraph(c, desc.strip(), 40, y, width)

            y -= 10

    # ---------- CERTIFICATIONS ----------
    if student.get("certifications"):
        section("Certifications")
        count = 1
        for cert in student["certifications"]:
            y = check_page_space(c, y)
            c.setFont("Helvetica", 10)
            c.drawString(40, y, f"{count}. {cert}")
            y -= 15
            count += 1
        y -= 5

    # ---------- DECLARATION ----------
    if student.get("declaration"):
        section("Declaration")
        y = draw_paragraph(c, student["declaration"], 40, y, width)

    c.save()
    return filename
