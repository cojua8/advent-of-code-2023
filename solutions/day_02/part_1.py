from solutions.common.file_reader import read_file_lines


def get_game_number(game_description: str) -> int:
    return int(game_description.split(" ")[1])


def get_game_info(game: str) -> dict[str, int]:
    game_info: dict[str, int] = {}
    for revealed in game.split(","):
        number, color = revealed.strip().split(" ")
        game_info[color] = int(number)

    return game_info


def get_revealed_numbers(games: str):
    game_list = games.split(";")
    return [get_game_info(game) for game in game_list]


def process_line(line: str):
    game_description, games = line.split(":")

    return get_game_number(game_description), get_revealed_numbers(games)


def check_possible_reveal(
    revealed: dict[str, int], total_balls: dict[str, int]
) -> bool:
    for color in revealed:
        if revealed[color] > total_balls[color]:
            return False
    return True


def check_possible_game(
    game: list[dict[str, int]], total_balls: dict[str, int]
) -> bool:
    return all(check_possible_reveal(revealed, total_balls) for revealed in game)


if __name__ == "__main__":
    existing_balls = {"red": 12, "green": 13, "blue": 14}
    ids_sum = 0

    for line in read_file_lines("day_02.txt"):
        game_number, games = process_line(line)

        if check_possible_game(games, existing_balls):
            ids_sum += game_number

    print(ids_sum)
