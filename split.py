import re
from pprint import pprint


def simplify_text(text: str) -> str:
    # remove just use index from '^\d\d\/\d\d\\/2024\n' to index of '^Page\s' with regex
    temp = re.search(r"(?<=\n)\d{2}\/\d{2}\/2024(?=\n\d+)", text)
    assert temp is not None, "No date found"
    start_content = temp.start()
    temp = re.search(r"Page\s\d+", text)
    if temp is None:
        # end position is end of string
        end_content = len(text)
    else:
        end_content = temp.start()

    return text[start_content:end_content]


def split_entries(text: str) -> list[str]:
    # split by date with regex, not remove date in result
    entries = re.split(r"\n(?=\d{2}\/\d{2}\/2024\n)", text)
    assert entries, "No entries found"
    return entries[1:]


def parse_entry(entry: str) -> dict:
    lines = entry.split("\n")
    assert len(lines) >= 4, f"Invalid entry: {entry}"
    date = lines[0]
    no = lines[1]
    amount = lines[2]
    detail = None

    # temprary ignore balance
    detail = " ".join(lines[3:])

    return {
        "date": date,
        "no": no,
        "amount": amount,
        "detail": detail,
    }


def main():
    with open("output_5292.txt", "r") as file:
        text = file.read()

    text = simplify_text(text)
    entries = split_entries(text)

    for entry in entries[:-1]:
        result = parse_entry(entry)
        print(result)


if __name__ == "__main__":
    main()
