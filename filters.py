import sys


def filter_files(name: str, function) -> None:
    with open(name) as input_, open(name + '.out', 'w') as output:
        list(map(lambda line: output.write(function(line)), input_))


def filter_stream(function) -> None:
    list(map(lambda line: print(line, end=''), sys.stdin))


def main():
    filter_stream(lambda line: line)


if __name__ == '__main__':
    main()
