import threading


class Foo:
    def __init__(self):
        self.second_lock = threading.Lock()
        self.second_lock.acquire()
        self.third_lock = threading.Lock()
        self.third_lock.acquire()

    def first(self):
        # printFirst() outputs "first". Do not change or remove this line.
        print('first')
        self.second_lock.release()

    def second(self):
        # printSecond() outputs "second". Do not change or remove this line.
        with self.second_lock:
            print('second')
            self.third_lock.release()

    def third(self):
        # printThird() outputs "third". Do not change or remove this line.
        with self.third_lock:
            print('third')


a = Foo()
t1 = threading.Thread(target=a.third)
t2 = threading.Thread(target=a.second)
t3 = threading.Thread(target=a.first)

t1.start()
t2.start()
t3.start()
