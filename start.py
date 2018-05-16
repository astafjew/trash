import os

dirname = '.'


def print_filepath(filename: str) -> None:
    print(os.path.abspath(filename))


[print_filepath(file) for file in os.listdir(dirname)]
