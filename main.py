from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv('topics.csv')

page_number = 0

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 12, row['Topic'], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    for i in range(20, 280, 12):
        pdf.line(10, i, 200, i)

    pdf.ln(260)
    page_number += 1

    # Set a footer for the page
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 12, txt=f"{row['Order']} {row['Topic']} Page: {page_number}", align="R", ln=1)

    for page in range(int(row['Pages'])-1):
        pdf.add_page()
        page_number += 1

        for i in range(20, 280, 12):
            pdf.line(10, i, 200, i)

        # Set the footer for the page
        pdf.ln(272)
        pdf.set_font('Arial', 'I', 8)
        pdf.cell(0, 12, txt=f"{row['Order']} {row['Topic']} Page: {page_number}", align="R", ln=1)

pdf.output('output.pdf')
