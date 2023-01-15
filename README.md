# PDF Splitter

I wrote this tiny script to split one PDF page into multiple pages.

## Getting Started

### Preperation

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Copy the PDF that needs to be splitted into the same directory as the script

### Run the application

Use the parameter `--help` to view the instructions.

```shell
❯ python pdf_splitter.py -h
usage: pdf_splitter.py [-h] filename pages

Takes a list of pages and splits a PDF

positional arguments:
  filename
  pages       Pages as comma separated list. The number indicates a new PDF file.

options:
  -h, --help  show this help message and exit
```

### Example

The parameter `pages` is a comma-separated list of page numbers to identify the first page of each new PDF file.
So if you have a PDF with 10 pages and you want the new pages to contain
1. 1st PDF page 1-2
2. 2nd PDF page 3-6
3. 3rd PDF page 7-10

Then the command is `python pdf_splitter.py FILENAME 1,3,7`

****

Have fun!

****
