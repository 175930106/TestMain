#!/usr/bin/python
# -*- coding: UTF-8 -*-

from threading import Thread
from time import ctime,sleep
from ctypes.test.test_errno import threading

global_num = 0
 
def func1():
    global global_num
    for i in range(1000000):
        global_num += 1
    print('---------func1:global_num=%s--------'%global_num)
 
def func2():
    global global_num
    for i in range(1000000):
        global_num += 1
    print('--------fun2:global_num=%s'%global_num)
print('global_num=%s'%global_num)
 

 
t1 = Thread(target=func1)
t1.start()
 
t2 = Thread(target=func2)
t2.start()

print threading.current_thread()
print "t1==getName",t1.getName()
print "t1==is_alive",t1.is_alive()
print threading.current_thread()
print "t2==getName",t2.getName()
print "t2==is_alive",t2.is_alive()
print threading.enumerate()