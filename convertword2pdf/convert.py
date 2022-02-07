from docx2pdf import convert
import os
path = os.listdir("D:\documents\Python Scripts\convertword2pdf")

# demo for 1 file
#convert("C:/Users/pi/Desktop/docx2pdf/testfile1.docx",
  #"C:/Users/pi/Desktop/docx2pdf/output1.pdf")

for i, files in enumerate(path):
    if files[-5:] == '.docx':
        convert(f"D:\documents\Python Scripts\convertword2pdf/try.docx",
         f"D:\documents\Python Scripts\convertword2pdf/output.pdf")