from enum import Enum
from aoc.utils import read_input
import re


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Limit(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14


def parse_sets(sets: str):
    separate_colors = map(lambda s: s.split(","), sets.split(";"))
    return list(separate_colors)


def parse_game(game: str):
    pattern = r"Game (\d+): ([a-zA-Z0-9\s,;]+)"
    regex = re.compile(pattern)
    matching = re.search(regex, game)
    if matching:
        id = matching.group(1)
        sets = matching.group(2)
        return int(id), parse_sets(sets)


def swap(tup: tuple):
    a, b = tup
    return b, a


def second_as_int(tup: tuple):
    a, b = tup
    return a, int(b)


def get_counts(ls_colors: list[str]):
    stripped = map(lambda s: s.strip(), ls_colors)
    to_tuple = map(lambda s: second_as_int(swap(tuple(s.split(" ")))), stripped)
    return dict(to_tuple)


def check_limits(counter: dict):
    return (
        (counter.get(Color.RED.value, 0) <= Limit.RED.value)
        & (counter.get(Color.BLUE.value, 0) <= Limit.BLUE.value)
        & (counter.get(Color.GREEN.value, 0) <= Limit.GREEN.value)
    )


def solve(input):
    possible_ids = filter(lambda x: x is not None, map(check_possible_game, input))
    return sum(possible_ids)


def check_possible_game(input_element):
    id, game = parse_game(input_element)
    counts = list(map(get_counts, game))
    checking_limits = all(map(check_limits, counts))
    if checking_limits:
        return id


def main():
    games_input = read_input("day02/input")
    result = solve(games_input)
    print(result)


if __name__ == "__main__":
    main()
