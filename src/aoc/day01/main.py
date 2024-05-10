from typing import TypeVar, Iterable
from aoc.utils import read_input

T = TypeVar("T")


def is_digit(num: str) -> bool:
    return num.isdigit()


def first(predicate, iterable: Iterable[T]) -> T:
    return next(filter(predicate, iterable))


def extract_first_digit(s: str) -> int:
    return first(is_digit, list(s))


def extract_digits(s: str) -> int:
    first_digit = extract_first_digit(s)
    second_digit = extract_first_digit(reversed(s))
    digits = f"{first_digit}{second_digit}"
    return int(digits)


def solve(lines: list[str]) -> int:
    result = map(extract_digits, lines)
    return sum(result)


def main():
    text = read_input("day01/input")
    result = solve(text)
    print(result)


if __name__ == "__main__":
    main()
