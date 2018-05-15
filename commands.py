import sys
import scanner as scan


class UnknownCommand(Exception):
    pass


def proccess_line(line):
    commands = {'*': 'Ms.', '+': 'Mr.'}
    try:
        print(commands[line[0]], line[1:], end='')
    except KeyError:
        raise UnknownCommand(line)


def main():
    filename = 'data.txt'
    scan.scanner(filename, proccess_line)


if __name__ == '__main__':
    main()
