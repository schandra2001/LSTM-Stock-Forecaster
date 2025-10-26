import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def parse_resume(text):
    name = re.findall(r"Name[:\s]+(.+)", text)
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"\+?\d[\d\s\-()]{7,}\d", text)
    skills = re.findall(r"Skills[:\s]+(.+)", text)

    return {
        "Name": name[0] if name else "Not found",
        "Email": email[0] if email else "Not found",
        "Phone": phone[0] if phone else "Not found",
        "Skills": skills[0].split(",") if skills else []
    }

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("sample_resume.pdf")
    parsed_data = parse_resume(resume_text)
    for key, value in parsed_data.items():
        print(f"{key}: {value}")
