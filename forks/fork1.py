import os


def child() -> None:
    print('Hello from child', os.getpid())
    os._exit(0)


def parent() -> None:
    while True:
        newipd = os.fork()
        if newipd is 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() is 'q':
            break
