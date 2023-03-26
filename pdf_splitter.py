#!/usr/bin/env python
import argparse
import pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter

# Method to split the pdf at every given n pages.
def split_pdf(filename: str, pages: str):


    filepath = pathlib.Path(filename)
    new_filename = filename[:-4]

    input_file = open(filepath, 'rb')
    pdf_org = PdfFileReader(input_file)

    # Get pages
    new_first_pages = [int(i) for i in pages.split(',')]
    
    new_file = None
    pdf_page_count = pdf_org.getNumPages()
    for i in range(pdf_page_count):
        if i+1 in new_first_pages:
            if new_file is not None:
                # write to file
                with open(f"{new_filename}_{i}.pdf", "wb") as output_stream:
                    new_file.write(output_stream)
            new_file = PdfFileWriter()
        # Add to page
        new_file.addPage(pdf_org.getPage(i))

    # write last file
    with open(f"{new_filename}_{i+1}.pdf", "wb") as output_stream:
        new_file.write(output_stream)

if __name__ == "__main__":
    # Local execution
    parser = argparse.ArgumentParser(prog = 'pdf_splitter.py', description = 'Takes a list of pages and splits a PDF')

    parser.add_argument('filename')
    parser.add_argument('pages', help="Pages as comma separated list. The number indicates a new PDF file.")

    args = parser.parse_args()

    split_pdf(args.filename, args.pages)