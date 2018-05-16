def scanner(name: str, function) -> None:
    list(map(function, open(name)))


def main():
    scanner('spam.txt', lambda l: print(l, end=''))


if __name__ == '__main__':
    main()
