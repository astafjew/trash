import _thread
import time


def imitate_exec(id_: int, count: int) -> None:
    time.sleep(1)
    print(f'[{id_}] => {count}')


def counter(id_: int, count: int) -> None:
    [imitate_exec(id_, i) for i in range(count)]


[_thread.start_new_thread(counter, (i, 5)) for i in range(5)]
time.sleep(6)
print('Main thread exiting.')
