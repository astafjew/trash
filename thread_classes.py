import threading


class CustomThread(threading.Thread):
    def __init__(self, id_, count, mutex):
        self.id = id_
        self.count = count
        self.mutex = mutex
        super().__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print(f'[{self.id}] => {i}')


stdout_mutex = threading.Lock()
threads = []

for i in range(10):
    thread = CustomThread(i, 100, stdout_mutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('Main thread exiting.')
