import re
from typing import NamedTuple
from solutions.common.file_reader import read_file_lines
from re import Match


class Corner(NamedTuple):
    row: int
    col: int


class Box(NamedTuple):
    upper_left: Corner
    bottom_right: Corner


class Number(NamedTuple):
    value: int
    box: Box


def get_matches(line: str, pattern: str) -> list[Match[str]]:
    return [match for match in re.finditer(pattern, line)]


def get_number_matches(line: str) -> list[Match[str]]:
    pattern = r"\d+"
    return get_matches(line, pattern)


def get_symbols(line: str) -> list[Match[str]]:
    pattern = r"[^\.a-zA-Z0-9_]"
    return get_matches(line, pattern)


def get_box(line_number: int, number: Match[str]) -> Box:
    span_min, span_max = number.span()

    upper_left = Corner(max(0, line_number - 1), span_min - 1)
    bottom_right = Corner(line_number + 1, span_max)

    return Box(upper_left, bottom_right)


def get_numbers(line: str, line_number: int) -> list[Number]:
    return [
        Number(int(match.group()), get_box(line_number, match))
        for match in get_number_matches(line)
    ]


def get_symbol_positions(line: str) -> list[int]:
    symbols = get_symbols(line)
    return [symbol.span()[0] for symbol in symbols]


def is_part_number(number: Number, symbol_positions: list[list[int]]) -> bool:
    box = number.box

    for symbols in symbol_positions[box.upper_left.row : box.bottom_right.row + 1]:
        if any(box.upper_left.col <= v <= box.bottom_right.col for v in symbols):
            return True

    return False


if __name__ == "__main__":
    engine = read_file_lines("day_03.txt")

    numbers: list[Number] = []
    symbols: list[list[int]] = []
    for line_number, line in enumerate(engine):
        numbers.extend(get_numbers(line, line_number))
        symbols.append(get_symbol_positions(line))

    print(sum([number.value for number in numbers if is_part_number(number, symbols)]))
