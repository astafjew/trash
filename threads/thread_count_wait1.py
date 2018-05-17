import _thread
stdout_mutex = _thread.allocate_lock()
exit_mutexes = [_thread.allocate_lock()
                for i in range(10)]


def counter(id_: int, count: int) -> None:
    for i in range(count):
        stdout_mutex.acquire()
        print(f'[{id_}] => {i}')
        stdout_mutex.release()
    exit_mutexes[id_].acquire()


[_thread.start_new_thread(counter, (i, 100))
 for i in range(10)]

for mutex in exit_mutexes:
    while not mutex.locked():
        pass
print('Main thread exiting.')
