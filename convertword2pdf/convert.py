from docx2pdf import convert
import os
path = os.listdir("C:/Users/ACER/AppData/Local/Programs/Python/Python39/Lib/site-packages/docx2pdf/convert")

# demo for 1 file
#convert("C:/Users/pi/Desktop/docx2pdf/testfile1.docx",
  #"C:/Users/pi/Desktop/docx2pdf/output1.pdf")

for i, files in enumerate(path):
    if files[-5:] == '.docx':
        convert(f"C:/Users/ACER/AppData/Local/Programs/Python/Python39/Lib/site-packages/docx2pdf/convert/try.docx",
         f"C:/Users/ACER/AppData/Local/Programs/Python/Python39/Lib/site-packages/docx2pdf/convert/output.pdf")
