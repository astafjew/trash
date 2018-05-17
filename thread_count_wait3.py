import _thread
import time

stdout_mutex = _thread.allocate_lock()
num_threads = 5
exit_mutexes = [_thread.allocate_lock()
                for i in range(num_threads)]


def counter(id_: int, count: int,
            mutex: _thread.LockType) -> None:
    for i in range(count):
        time.sleep(1/(id_+1))
        with mutex:
            print(f'[{id_}] => {i}')
    exit_mutexes[id_].acquire()


[_thread.start_new_thread(counter, (i, 5, stdout_mutex))
 for i in range(num_threads)]

while not all(mutex.locked() for mutex in exit_mutexes):
    time.sleep(0.25)
print('Main thread exiting.')
