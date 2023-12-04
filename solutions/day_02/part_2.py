from functools import reduce
from solutions.common.file_reader import read_file_lines


def get_game_number(game_description: str) -> int:
    return int(game_description.split(" ")[1])


def get_game_info(game: str) -> dict[str, int]:
    game_info: dict[str, int] = {}
    for revealed in game.split(","):
        number, color = revealed.strip().split(" ")
        game_info[color] = int(number)

    return game_info


def get_revealed_numbers(games: str) -> list[dict[str, int]]:
    game_list = games.split(";")
    return [get_game_info(game) for game in game_list]


def process_line(line: str) -> tuple[int, list[dict[str, int]]]:
    game_description, games = line.split(":")

    return get_game_number(game_description), get_revealed_numbers(games)


def get_minimum_number_of_cubes(game: list[dict[str, int]]) -> dict[str, int]:
    total_cubes = {"red": 0, "green": 0, "blue": 0}

    for revealed in game:
        for color in revealed:
            if revealed[color] > total_cubes[color]:
                total_cubes[color] = revealed[color]

    return total_cubes


if __name__ == "__main__":
    existing_cubes = {"red": 12, "green": 13, "blue": 14}
    power_sum = 0

    for line in read_file_lines("day_02.txt"):
        game_number, games = process_line(line)

        power = reduce(lambda x, y: x * y, get_minimum_number_of_cubes(games).values())

        power_sum += power

    print(power_sum)
