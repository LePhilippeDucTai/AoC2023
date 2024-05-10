from pathlib import Path


def read_input(file_path):
    datadir = get_data_dir()
    filepath = datadir / file_path
    with open(filepath, "r") as file:
        return file.read().splitlines()


def get_data_dir():
    return Path(__file__).parent.parent.parent / "data"
