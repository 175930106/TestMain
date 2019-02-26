#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps  = {}
desired_caps ["platformName"] = "Android"
desired_caps ["platformVersion"] = "7.0"
desired_caps ["deviceName"] = "5LM0215C28006846"
desired_caps ["appPackage"] = "com.tencent.mm"
desired_caps ["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps ["noReset"] = True
#设置未接收到新命令的超时时间，默认60s
desired_caps ["newCommandTimeout"]=300
#Appium是否要自动启动或安装app，默认true
# desired_caps ['autoLaunch'] = 'false'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps )

driver.implicitly_wait(10)
print driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']")
print driver.app_strings
print driver.current_activity

#音量操作
for i in range(0,5,1):
    driver.press_keycode(24)
    
for j in range(0,5,1):
    driver.press_keycode(25)

driver.is_app_installed('com.ibox.calculators.CalculatorActivity')
driver.wait_activity('com.ibox.calculators.CalculatorActivity', 2, 2)
driver.implicitly_wait(10)
#下拉操作
# TouchAction(driver).press(x=462, y=345).wait(500).move_to(x=462, y=1219).wait(500).release().perform()
width = driver.get_window_size('current')['width']
height= driver.get_window_size('current')['height']

driver.swipe(width/2, height/4, width/2, height*3/4, 500)
#self.assertEqual(self.driver.find_element_by_id('com.boohee.secret:id/tv_title').text,u'超模25','切到超模25tab失败')
print driver.page_source,type('driver.page_source'),driver.page_source.find(u'商户通')
print driver.current_context

driver.implicitly_wait(10)
i="//android.support.v7.widget.RecyclerView[@resource-id='com.tencent.mm:id/o_']/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]"
driver.find_element_by_xpath(i).click()
j="//android.view.View[@content-desc='今日销售量']"
print 'contentDescription',driver.find_element_by_xpath(j).get_attribute('contentDescription')
print 'resourceId',driver.find_element_by_xpath(j).get_attribute('resourceId')
print 'className',driver.find_element_by_xpath(j).get_attribute('className')
print 'text',driver.find_element_by_xpath(j).get_attribute('text')
print 'checkable',driver.find_element_by_xpath(j).get_attribute('checkable')
print 'clickable',driver.find_element_by_xpath(j).get_attribute('clickable')
print 'enabled',driver.find_element_by_xpath(j).get_attribute('enabled')
driver.find_element_by_xpath(j).click()
# print driver.find_element_by_xpath("//android.widget.TextView[@text='e商户通']").is_displayed()


