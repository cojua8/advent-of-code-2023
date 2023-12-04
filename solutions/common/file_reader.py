from pathlib import Path


def read_file_lines(file: str) -> list[str]:
    file = Path("input_files") / file

    return file.read_text().split("\n")
