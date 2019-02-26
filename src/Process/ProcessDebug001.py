#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
import time

_global_priority=1

def _p(_global_priority):
        if _global_priority == 1:
            raise NameError
        else:
            raise ValueError
        
print _p(2)