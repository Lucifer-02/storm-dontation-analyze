import fitz
import polars as pl

from split import simplify_text, split_entries, parse_entry


def text_extract(pdf_file: str) -> list[str]:
    doc = fitz.open(pdf_file)

    content = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text()
        content.append(page_text)

    return content


def main():
    pdf_file = "./Thong tin ung ho qua TSK VCB 0011001932418 tu 01.09 den10.09.2024.pdf"
    content = text_extract(pdf_file)

    df = pl.DataFrame()

    dates = []
    nos = []
    amounts = []
    details = []

    for i, page_text in enumerate(content):
        text = simplify_text(page_text)
        entries = split_entries(text)
        for entry in entries:
            print(f"Page {i + 1}")
            result = parse_entry(entry)
            dates.append(result["date"])
            nos.append(result["no"])
            amounts.append(result["amount"])
            details.append(result["detail"])

    df = pl.DataFrame(
        {
            "no": nos,
            "date": dates,
            "amount": amounts,
            "detail": details,
        }
    )

    df.write_csv("output.csv")


if __name__ == "__main__":
    main()
