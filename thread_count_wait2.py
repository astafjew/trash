import _thread
stdout_mutex = _thread.allocate_lock()
exit_mutexes = [False] * 10


def exec_lock(function) -> None:
    stdout_mutex.acquire()
    function()
    stdout_mutex.release()


def counter(id_: int, count: int) -> None:
    for i in range(count):
        exec_lock((lambda: print(f'[{id_}] => {i}')))
    exit_mutexes[id_] = True


[_thread.start_new_thread(counter, (i, 100))
 for i in range(10)]

while False in exit_mutexes:
    pass

print('Main thread exiting.')
