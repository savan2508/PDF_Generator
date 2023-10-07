import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    filename = Path(filepath).stem
    invoice_number, date = filename.split("-")

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(False, margin=0)
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    pdf.cell(0, 12, txt=f"Invoice No. {invoice_number}", align="L", ln=1)
    pdf.cell(0, 12, txt=f"Date: {date}", align="L", ln=1)

    # Add a header of the table
    columns = list(df.columns)
    columns = [column.replace("_", " ").title() for column in columns]

    pdf.set_font('Arial', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(30, 8, txt=f"{columns[0]}", border=1, fill=True)
    pdf.cell(70, 8, txt=f"{columns[1]}", border=1, fill=True)
    pdf.cell(30, 8, txt=f"{columns[2]}", border=1, fill=True)
    pdf.cell(30, 8, txt=f"{columns[3]}", border=1, fill=True)
    pdf.cell(30, 8, txt=f"{columns[4]}", border=1, fill=True, ln=1)

    # Add the data to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Arial", size=8)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(30, 8, txt=f"{row['product_id']}", border=1)
        pdf.cell(70, 8, txt=f"{row['product_name']}", border=1)
        pdf.cell(30, 8, txt=f"{row['amount_purchased']}", border=1)
        pdf.cell(30, 8, txt=f"{row['price_per_unit']}", border=1)
        pdf.cell(30, 8, txt=f"{row['total_price']}",border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
