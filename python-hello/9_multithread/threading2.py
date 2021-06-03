import threading
from threading import current_thread

# threading.Thread().run()
# 类的方式实现多线程编程
class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')

t1 = MyThread()
t1.start()
t1.join()
print(current_thread().getName(), 'end')