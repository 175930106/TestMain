#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
import time



class Testaa2(unittest.TestCase):
    u'''测试用例a的集合'''
#     @classmethod
#     def setUpClass(cls):
# #         cls.driver = webdriver.Chrome()
#         print "testfile demo3"

    def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://www.cnblogs.com/yoyoketang/")
        print "demodemo2etUp"

    def test_001(self):
#         u'''用例1：用例1的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)
        print " demo3--test_01"

    def test_002(self):
#         u'''用例2：用例2的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)
        print " demo3--test_02"
    def test_003(self):
#         u'''用例3：用例3的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn(u"悠悠", t)
        print " demo3--test_03"
#     def tearDown(self):
#         self.driver.quit()
        
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

if __name__ == "__main__":
    unittest.main()