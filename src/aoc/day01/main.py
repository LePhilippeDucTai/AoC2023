from aoc.utils import read_input


def is_digit(num: str):
    return num.isdigit()


def first(predicate, iterable):
    return next(filter(predicate, iterable))


def extract_first_digit(s: str):
    return first(is_digit, list(s))


def extract_digits(s: str):
    first_digit = extract_first_digit(s)
    second_digit = extract_first_digit(reversed(s))
    digits = f"{first_digit}{second_digit}"
    return int(digits)


def solve(lines: list[str]):
    result = map(extract_digits, lines)
    return sum(result)


def main():
    text = read_input("day01/input")
    result = solve(text)
    print(result)


if __name__ == "__main__":
    main()
