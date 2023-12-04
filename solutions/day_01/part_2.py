import regex
from solutions.common.file_reader import read_file_lines

pattern = r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)"

word_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_numbers(text: str) -> list[str]:
    return [
        word_to_number.get(match) or match
        for match in regex.findall(pattern, text, overlapped=True)
    ]


if __name__ == "__main__":
    calibration_sum = 0

    for line in read_file_lines("day_01_2.txt"):
        numbers = get_numbers(line)

        calibration_value = int(numbers[0] + numbers[-1])

        calibration_sum += calibration_value

    print(calibration_sum)
