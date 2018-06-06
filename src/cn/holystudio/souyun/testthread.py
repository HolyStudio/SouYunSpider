__author__ = 'chenqingsen'

from src.cn.holystudio.files import configfile

cfg = configfile.ConfigFile()
cfg.init_config("config.ini")

domain  = cfg.get_config("WebConfig","Domain")
yunListUrl = cfg.get_config("WebConfig","Url")

import _thread
import  threading

def print_time(threadName,delay):
    print("print_time>>>>>>")
    count =0
    while count<5:
        time.sleep(delay)
        count +=1
        print("%s:%s" %(threadName,time.ctime(time.time())))

try:
    print(">>>>>>")
    #thread = threading.Thread()
    #thread.start()
    #_thread._start_new_thread(print_time,("thread-0",2,))
    _thread._start_new_thread(print_time,("thread-1",2))
    _thread._start_new_thread(print_time,("thread-2",4))
except:
    print("Error:unable to start thread>>")

print(3/2)
print(3//2)
print(3*2)
print(3**2)




