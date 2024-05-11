from aoc.utils import read_input
import re
import pandas as pd
import functools as ft
import operator as op


class Color:
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Limit:
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
        (counter.get(Color.RED, 0) <= Limit.RED)
        & (counter.get(Color.BLUE, 0) <= Limit.BLUE)
        & (counter.get(Color.GREEN, 0) <= Limit.GREEN)
    )


def solve(input):
    possible_ids = filter(lambda x: x is not None, map(check_possible_game, input))
    return sum(possible_ids)


def check_possible_game(input_element):
    id, counts = compute_counts(input_element)
    checking_limits = all(map(check_limits, counts))
    if checking_limits:
        return id


def compute_counts(input_element):
    id, game = parse_game(input_element)
    counts = list(map(get_counts, game))
    return id, counts


def merge_max_dicts(d1: dict, d2: dict) -> dict:
    max_dict = pd.DataFrame([d1, d2]).fillna(0).astype("int").max().to_dict()
    return max_dict


def power(sets: dict):
    return ft.reduce(op.mul, sets.values())


def max_counts(input_element):
    _, counts = compute_counts(input_element)
    max_dicts = ft.reduce(merge_max_dicts, counts)
    return power(max_dicts)


def solve_part2(games_input):
    powers = map(max_counts, games_input)
    return sum(powers)


def main():
    games_input = read_input("day02/input")
    result = solve(games_input)
    print(f"Part 1: {result}")

    result_2 = solve_part2(games_input)
    print(f"Part 2: {result_2}")


if __name__ == "__main__":
    main()
