#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "5LM0215C28006846"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = "com.tencent.mm.plugin.appbrand.ui.AppBrandUI"
caps["noReset"] = True
#设置未接收到新命令的超时时间，默认60s
caps["newCommandTimeout"]=300
#Appium是否要自动启动或安装app，默认true
# caps['autoLaunch'] = 'false'

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# el4 = driver.find_element_by_id("com.ibox.calculators:id/digit1")
# el4.click()
# el5 = driver.find_element_by_id("com.ibox.calculators:id/plus")
# el5.click()
# el6 = driver.find_element_by_id("com.ibox.calculators:id/digit9")
# el6.click()
# el7 = driver.find_element_by_id("com.ibox.calculators:id/equal")
# el7.click()


a1=driver.find_element_by_android_uiautomator('text("1")')
a1.click()

a2=driver.find_element_by_android_uiautomator('text("+")')
a2.click()

a3=driver.find_element_by_android_uiautomator('text("9")')
a3.click()

driver.lock(5)

print driver.is_app_installed('com.ibox.calculators')

a4=driver.find_element_by_android_uiautomator('text("=")')
a4.click()
# driver.quit()