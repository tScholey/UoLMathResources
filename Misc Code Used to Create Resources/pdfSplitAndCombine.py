from pdfrw import *
import os

cwd = os.getcwd()

def concatenate(input_file_paths, output_file_name):
    writer = PdfWriter()
 
    for path in paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)
 
    writer.trailer.Info = IndirectPdfDict(
        Title='Title Here',
        Author='Author Here',
        Subject= 'Subject Here',
        Creator='Creator Here'
    )
 
    writer.write(output_file_name)


def splitPdf(input_file_path,output_file1_pages,output_file1_name,output_file2_pages,output_file2_name):
    reader_input = PdfReader(input_file_path)
    writer_output1 = PdfWriter()
    writer_output2 = PdfWriter()
    for current_page in range(len(reader_input.pages)):
        if current_page in output_file1_pages:
            writer_output1.addpage(reader_input.pages[current_page])
        elif current_page in output_file2_pages:
            writer_output2.addPage(reader_input.pages[current_page])
    writer_output1.write(output_file1_name)
    writer_output2.write(output_file2_name)
