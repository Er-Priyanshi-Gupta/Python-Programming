import PyPDF2 
import os
mergeFiles = PyPDF2.PdfMerger()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for file in files:
    mergeFiles.append(file)
mergeFiles.write("Combined-files.pdf")
mergeFiles.close()