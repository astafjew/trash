import _thread
import time

mutex = _thread.allocate_lock()


def exec_with_lock(function) -> None:
    mutex.acquire()
    function()
    mutex.release()


def imitate_exec(id_: int, count: int) -> None:
    time.sleep(1)
    exec_with_lock((lambda: print(f'[{id_}] => {count}')))


def counter(id_: int, count: int) -> None:
    [imitate_exec(id_, i) for i in range(count)]


[_thread.start_new_thread(counter, (i, 5)) for i in range(5)]
time.sleep(6)
print('Main thread exiting.')
