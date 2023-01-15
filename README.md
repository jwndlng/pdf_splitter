# PDF Splitter

I wrote this tiny script to split one PDF page into multiple pages.

## Getting Started

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Copy the PDF that needs to be splitted into the same directory as the script
3. Run the application `python pdf_splitter.py [-h] filename pages`

The pages are a comma-separated list of page numbers to identify the first page of each new PDF file.
E.g. You have a PDF with 10 pages and you want the new pages to contain
1. 1st PDF page 1-2
2. 2nd PDF page 3-6
3. 3rd PDF page 7-10

Then the command is `python pdf_splitter.py FILENAME 1,3,7

## Have fun!