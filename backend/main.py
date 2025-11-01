import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import dropbox


if not os.path.exists("reports"):
    os.makedirs("reports")


df = pd.read_csv("data/data.csv")

summary = df.groupby("categoria")["valor"].sum()


plt.figure(figsize=(6,4))
summary.plot(kind="bar", color='skyblue')
plt.title("Resumo por Categoria")
plt.ylabel("Valor")
plt.tight_layout()
plt.savefig("reports/chart.png")
plt.close()


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Relatório Diário", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", size=12)
for cat, val in summary.items():
    pdf.cell(0, 10, txt=f"{cat}: {val}", ln=True)

pdf.image("reports/chart.png", x=10, y=60, w=180)
pdf_file_path = "reports/report.pdf"
pdf.output(pdf_file_path)

print(f"PDF gerado: {pdf_file_path}")


# Dropbox


with open("credentials/dropbox_token.txt", "r") as f:
    DROPBOX_TOKEN = f.read().strip()

dbx = dropbox.Dropbox(DROPBOX_TOKEN)


dropbox_path = "/relatorios/report.pdf"

with open(pdf_file_path, "rb") as f:
    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

print(f"PDF enviado para o Dropbox! Caminho: {dropbox_path}")
