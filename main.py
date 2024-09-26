import pandas as pd
import openpyxl
import glob
from fpdf import FPDF
from pathlib import Path

# openpyxl is a Python library to read/write Excel files
# glob allows you to search for files with specific patterns

# get all files ending with .xlsx
text_files = glob.glob("text_files/*.txt")

# create pdf format
pdf = FPDF(orientation="P", unit="mm", format="A4")

for animal in text_files:

    pdf.add_page()

    # this pandas command only works with openpxyl downloaded
    df = pd.read_csv(animal)

    # extracting the name of the file
    filename = Path(animal).stem
    animal_name = filename.split("-")[0].capitalize()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name)


# create the pdf
pdf.output("output.pdf")
