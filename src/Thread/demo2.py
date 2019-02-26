#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
import time



class Testaa1(unittest.TestCase):
    u'''测试用例a的集合'''
#     @classmethod
#     def setUpClass(cls):
#         print "testfile demo2"
# #         cls.driver = webdriver.Chrome()

    def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://www.cnblogs.com/yoyoketang/")
        print "demo2---setUp"

    def test_01(self):
        print " demo2--test_01"
#         u'''用例1：用例1的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)


    def test_02(self):
        print " demo2--test_02"
#         u'''用例2：用例2的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)

    def test_03(self):
        print " demo2--test_03"
#         u'''用例3：用例3的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)

#     def tearDown(self):
#         self.driver.quit()
        
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

if __name__ == "__main__":
    unittest.main()