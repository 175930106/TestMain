#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import os,time
import threading
import multiprocessing
# from BeautifulReport import BeautifulReport
from tomorrow import threads 
import HTMLTestRunner
from common import commonMethods as common
com=common()


# 测试用例文件路径123
casepath = './'
# 测试文件名
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
    filename="E:\\EclipseWorkspace\\nong12test\\ProcessThread\\src\\Process\\"+now+testFile+"_result.html"
    fp=open(filename,'wb')   
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'搜索功能测试报告',
        description=u'用例执行情况：',
        verbosity = 2)
      
    runner.run(Testcase_suite)    
    fp.close()

    
if __name__ == "__main__":
#     set_priority用于根据用例等级过滤用例，为1时跑高级用例，为2时跑高级和中级用例，为3时跑所有用例
    com.set_priority(1)
    testSuite(casepath,rule)
    

#     pool = multiprocessing.Pool(processes=2)
#     rule1=["demo2.py"]
#     rule2=["demo3.py"]
#     process = []
#     p1=pool.apply_async(testSuite,args=("./", rule1))
#     p2=pool.apply_async(testSuite,args=("./", rule2))
#     process.append(p1)
#     process.append(p2)
# 关闭pool，使其不在接受新的任务。
#     pool.close() 
#     pool.join()

