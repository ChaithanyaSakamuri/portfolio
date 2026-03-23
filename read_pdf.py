import PyPDF2

try:
    with open(r"f:\SEM 6\PES319\DIGITAL PORTFOLIO\assets\images\cv.pdf", "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("pdf_out.txt", "w", encoding="utf-8") as out:
            out.write(text)
    print("Success")
except Exception as e:
    print("ERROR:", e)
