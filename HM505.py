import threading
import time
import random
from threading import Thread


def thread_func():
    a = random.randint(1, 1000)
    print(a)
    time.sleep(2)


for i in range(5):
    th = threading.Thread(target=thread_func)
    print(th.getName())
    th.start()
    th.join()

thread_func()


class create_threads(Thread):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def run(self):
        m = lambda a: random.randint(a, 100)
        print(m(self.a))


for i in range(5):
    thread = create_threads(1)
    print(thread.name)
    thread.start()
    thread.join()
