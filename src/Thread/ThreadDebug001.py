#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. TIME==%s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print "I was at the %s! TIME==%s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        print "current_thread()====",threading.current_thread()
        print "active_count()====",threading.active_count()
        print "enumerate()====",threading.enumerate()
        t.setDaemon(True)
        t.start()
    t.join()
    
    print "all over == %s" %ctime()