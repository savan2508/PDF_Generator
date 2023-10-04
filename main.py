from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 12, row['Topic'], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

pdf.output('output.pdf')
