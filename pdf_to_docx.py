from pdf2docx import Converter
pdf_file = 'example.pdf'
docx_file = 'example.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
