import os
import time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print(f'[{os.getpid()}] => {i}')


def main():
    for i in range(5):
        pid = os.fork()
        if pid is not 0:
            print(f'Process {pid} spawned.')
        else:
            counter(5)
            os._exit(0)
    print('Main process exiting.')


if __name__ == '__main__':
    main()
