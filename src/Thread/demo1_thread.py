#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import os,time
import threading

# from BeautifulReport import BeautifulReport
from tomorrow import threads 
import HTMLTestRunner

casepath = './'
rule=["demo2.py","demo3.py"]

def testSuite(case_path,rule):
    
    for i in range(len(rule)):
        discover = unittest.defaultTestLoader.discover(case_path,pattern=rule[i], top_level_dir=None)
        testReport(discover,rule[i])

    
def testReport(Testcase_suite,testFile):
    if "*" in testFile:
        testFile=testFile.replace("*.py","")
    else:
        testFile=testFile.replace(".py","")
        
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename="E:\\EclipseWorkspace\\nong12test\\ProcessThread\\src\\Thread\\"+now+testFile+"_result.html"
    fp=open(filename,'wb')   
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'搜索功能测试报告',
        description=u'用例执行情况：',
        verbosity = 2)
      
    runner.run(Testcase_suite)    
    fp.close()


# python的线程有GIL锁Global interpreter lockd，无论系统有多少cpu，同一个时间点上，只有一个线程运行:
# 在Python2.x里，GIL的释放逻辑是当前线程遇见IO操作或者ticks计数达到100（ticks可以看作是Python自身的一个计数器，
# 专门做用于GIL，每次释放后归零，这个计数可以通过 sys.setcheckinterval 来调整），进行释放。
# 而每次释放GIL锁，线程进行锁竞争、切换线程，会消耗资源。并且由于GIL锁存在，python里一个进程永远只能同时执行一个线程(拿到GIL的线程才能执行)，这就是为什么在多核CPU上，python的多线程效率并不高
# 1、CPU密集型代码(各种循环处理、计数等等)，在这种情况下，由于计算工作多，ticks计数很快就会达到阈值，然后触发GIL的释放与再竞争（多个线程来回切换当然是需要消耗资源的），所以python下的多线程对CPU密集型代码并不友好。        
# 2、IO密集型代码(文件处理、网络爬虫等)，多线程能够有效提升效率(单线程下有IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。
# 所以python的多线程对IO密集型代码比较友好。 
# 而在python3.x中，GIL不使用ticks计数，改为使用计时器（执行时间达到阈值后，当前线程释放GIL），这样对CPU密集型程序更加友好，但依然没有解决GIL导致的同一时间只能执行一个线程的问题，所以效率依然不尽如人意。                                      
# 请注意：多核多线程比单核多线程更差，原因是单核下多线程，每次释放GIL，唤醒的那个线程都能获取到GIL锁，所以能够无缝执行，但多核下，CPU0释放GIL后，其他CPU上的线程都会进行竞争，但GIL可能会马上又被CPU0拿到，
# 导致其他几个CPU上被唤醒后的线程会醒着等待到切换时间后又进入待调度状态，这样会造成线程颠簸(thrashing)，导致效率更低

# threads = []
# t1=threading.Thread(target=demo,args=("./","demo*.py"))
# t2=threading.Thread(target=demo,args=("./","demo3.py"))
# threads.append(t1)
# threads.append(t2)

#unittest框架如果用线程执行，可能会导致测试报告输入混乱
if __name__ == "__main__":

    testSuite(casepath,rule)
#     for t in threads:
# #         t.setDaemon(True)
#         t.start()
#         print "current_thread()====",threading.current_thread()
#         print "active_count()====",threading.active_count()
#         print "enumerate()====",threading.enumerate()
#     t1.setDaemon(True)
#     t1.start()
#     print "11enumerate()====",threading.enumerate()
# #     守护线程，与join对立，若主线程结束了，不管子线程是否结束都会结束
# #     t2.setDaemon(True)
# 
