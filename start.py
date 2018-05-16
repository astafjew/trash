import os

dirname = '.'


def print_filepath(filename: str) -> None:
    print(os.path.abspath(filename))


def print_all_filepath(dirname: str) -> None:
    [print_filepath(file) for file in os.listdir(dirname)]
