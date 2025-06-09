import io
import pdfplumber

def extract_text_from_pdf(resume_file):
    with pdfplumber.open(io.BytesIO(resume_file.read())) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text
