__author__ = 'chenqingsen'

import threading
import time


exitFlag=0
class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        #super().__init__(self)
        super().__init__()
        self.threadID= threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("starting "+ self.name)
        print_time(self.name,self.counter,10)



def print_time(threadname,delay,counter):
    print("threadname="+threadname)
    while counter:
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print("%s:%s %d" % (threadname,time.ctime(time.time()),counter))
        counter -=1


thread1=MyThread(1,"thread-1",1)
thread2=MyThread(2,"thread-2",2)


thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exit")