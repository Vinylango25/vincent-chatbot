import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    cv_text = extract_text_from_pdf("cv_vincent.pdf")
    with open("cv_text.txt", "w", encoding="utf-8") as f:
        f.write(cv_text)
    print("✅ CV text extracted to cv_text.txt")
