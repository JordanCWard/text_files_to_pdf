import glob
from fpdf import FPDF
from pathlib import Path

# Get all files ending with .xlsx
text_files = glob.glob("text_files/*.txt")
# Create one pdf document
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in text_files:

    pdf.add_page()

    # Extracting the name of the file
    filename = Path(filepath).stem
    animal_name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name, ln=1)

    # Get the content of each text file
    with open(filepath, "r") as file:
        content = file.read()

    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)



# Produce the pdf
pdf.output("output.pdf")
