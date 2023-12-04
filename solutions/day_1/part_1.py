from solutions.common.file_reader import read_file_lines


def get_first_digit(text: str) -> str:
    return next(character for character in text if character.isdigit())


def get_last_digit(text: str) -> str:
    for index in range(len(text)):
        character = text[-1 - index]
        if character.isdigit():
            return character

    return ""


if __name__ == "__main__":
    calibration_sum = 0

    for line in read_file_lines("day_1_1.txt"):
        first_digit = get_first_digit(line)

        last_digit = get_last_digit(line)

        calibration_value = int(first_digit + last_digit)

        calibration_sum += calibration_value

    print(calibration_sum)
