import fitz


def extract_tables_with_pymupdf(pdf_file):
    doc = fitz.open(pdf_file)

    page_num = 12028

    page = doc[page_num - 1]
    content = page.get_text()
    # print(content)

    # save to file
    with open(f"output_{page_num}.txt", "w") as file:
        file.write(content)


# Usage example
pdf_file = "./Thong tin ung ho qua TSK VCB 0011001932418 tu 01.09 den10.09.2024.pdf"
extract_tables_with_pymupdf(pdf_file)
