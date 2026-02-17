from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(student, job_desc):
    resume_text = " ".join(student["skills"] + student["projects"])
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_desc, convert_to_tensor=True)
    return round(util.cos_sim(emb1, emb2).item() * 100, 2)
