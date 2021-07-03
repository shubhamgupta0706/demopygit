from threading import Thread
from time import sleep


class Chrome(Thread):

    def run(self):
        for i in range(10):
            print("Chrome is running")
            sleep(1)


class PyCharm(Thread):
    def run(self):
        for i in range(15):
            print("PyCharm is running")
            sleep(1)


t1 = Chrome()
t2 = PyCharm()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print('Bye')