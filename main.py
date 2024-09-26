import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
# import openpyxl, might need to install it?

# openpyxl is a Python library to read/write Excel files
# glob allows you to search for files with specific patterns

# get all files ending with .xlsx
text_files = glob.glob("text_files/*.txt")

# create only one pdf document because it's outside the for loop
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in text_files:

    pdf.add_page()

    # this pandas command only works with openpxyl downloaded
    df = pd.read_csv(filepath)

    # extracting the name of the file
    filename = Path(filepath).stem
    animal_name = filename.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name, ln=1)


# create the pdf
pdf.output("output.pdf")
