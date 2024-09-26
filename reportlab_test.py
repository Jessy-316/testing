from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import sys


def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Add some text
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100,
                "Hello, this is a PDF document created using ReportLab!")

    #Add a line
    c.line(100, height - 110, 500, height - 110)

    #Save the PDF
    c.save()

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Python version:", sys.version)
    create_pdf("example.pdf")
    print("PDF created: example.pdf")

