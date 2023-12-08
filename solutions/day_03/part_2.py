from functools import reduce
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

    def is_neighbor(self, other: "Box") -> bool:
        expanded_box = Box(
            Corner(self.upper_left.row - 1, self.upper_left.col - 1),
            Corner(self.bottom_right.row + 1, self.bottom_right.col + 1),
        )

        return (
            expanded_box.upper_left.row <= other.bottom_right.row
            and expanded_box.bottom_right.row >= other.upper_left.row
            and expanded_box.upper_left.col <= other.bottom_right.col
            and expanded_box.bottom_right.col >= other.upper_left.col
        )


class Number(NamedTuple):
    value: int
    box: Box


def get_matches(line: str, pattern: str) -> list[Match[str]]:
    return [match for match in re.finditer(pattern, line)]


def get_number_matches(line: str) -> list[Match[str]]:
    pattern = r"\d+"
    return get_matches(line, pattern)


def get_gears(line: str) -> list[Match[str]]:
    pattern = r"\*"
    return get_matches(line, pattern)


def get_box(line_number: int, match: Match[str]) -> Box:
    span_min, span_max = match.span()

    upper_left = Corner(max(0, line_number), span_min)
    bottom_right = Corner(line_number, span_max - 1)

    return Box(upper_left, bottom_right)


def get_numbers(line: str, line_number: int) -> list[Number]:
    return [
        Number(int(match.group()), get_box(line_number, match))
        for match in get_number_matches(line)
    ]


def get_gear_boxes(line: str, line_number: int) -> list[Box]:
    symbols = get_gears(line)
    return [get_box(line_number, symbol) for symbol in symbols]


def get_neighboring_numbers(gear: Box, numbers: list[Number]) -> list[Number]:
    return [number for number in numbers if gear.is_neighbor(number.box)]


def calculate_gear_ratio(gear: Box, numbers: list[Number]) -> int:
    neighboring_numbers = get_neighboring_numbers(gear, numbers)
    if len(neighboring_numbers) > 1:
        return reduce(
            lambda x, y: x * y, (number.value for number in neighboring_numbers)
        )
    else:
        return 0


if __name__ == "__main__":
    engine = read_file_lines("day_03.txt")

    numbers: list[Number] = []
    gear_boxes: list[Box] = []
    for line_number, line in enumerate(engine):
        numbers.extend(get_numbers(line, line_number))
        gear_boxes.extend(get_gear_boxes(line, line_number))

    print(sum(calculate_gear_ratio(gear, numbers) for gear in gear_boxes))
