#!/usr/bin/python
# -*- coding: UTF-8 -*-
import chardet
import ConfigParser
import os
import json
import time
from appium import webdriver
from time import sleep
import ConfigParser
import requests
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_global_priority=1
class commonMethods(unittest.TestCase):

    def desired_caps(self,phoneType):
     
        desired_caps  = {}
        desired_caps ["platformName"] = eval(self.get_config('common', phoneType, 'platformName'))
        desired_caps ["platformVersion"] = eval(self.get_config('common', phoneType, 'platformVersion'))
        desired_caps ["deviceName"] = eval(self.get_config('common', phoneType, 'deviceName'))
        desired_caps ["appPackage"] = eval(self.get_config('common', phoneType, 'appPackage'))
        desired_caps ["appActivity"] = eval(self.get_config('common', phoneType, 'appActivity'))
        desired_caps ["noReset"] = eval(self.get_config('common', phoneType, 'noReset'))
        #设置未接收到新命令的超时时间，默认60s
        desired_caps ["newCommandTimeout"]=eval(self.get_config('common', phoneType, 'newCommandTimeout'))
        #Appium是否要自动启动或安装app，默认true
        # desired_caps ['autoLaunch'] = 'false'
        #建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps )
        
        return desired_caps 
    # def slide_down(driver):
    #     #下拉操作 可以用于解锁屏幕
    #     # TouchAction(driver).press(x=462, y=345).wait(500).move_to(x=462, y=1219).wait(500).release().perform()
    @unittest.skipIf(True,"P1 level")
    def runTest(self):
        pass

    def get_config(self,page,section, key):
        
        current_path=os.path.dirname(__file__)
        src_path=os.path.dirname(current_path)
        config_path=src_path+"\\config\\"
        page_config_path=config_path+page+".conf"
        
        try:
            if os.path.exists(page_config_path):
                print 'File exists!',page_config_path
            
            else:
                print 'Cannot find the file : %s,please have a check!' %page_config_path
        
           
            config = ConfigParser.ConfigParser()
            config.read(page_config_path)   
    #         查询有多少section
    #         print config.items(section)
    
            return config.get(section, key)
    
        except Exception,e:
            print Exception,":",e
    

    def swipe_Down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/2,height/4,width/2,height*3/4,500)
        time.sleep(3)
    
    def swipe_Up(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/2,height*3/4,width/2,height/4,500)
    
    def swipe_Left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width/4,height/2,width*3/4,height/2,500)
    
    def swipe_Rigth(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width*4/5,height/2,width/5,height/2,500)
    
    def tap_screen(self,a,b):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.tap([(a,b)], 500)
    
    def Wchat_entrance(self):
        #等待页面
    #     driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps )
        try: 
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']")
    
            self.swipe_Down()
            #等待点击商户通程序
            self.driver.implicitly_wait(10)
    #       使用xpath父节点查找子节点
            i="//*[contains(@text,'体验版')]/../android.widget.ImageView"
    #       i和i1位置相同,i1更精确,直接通过名字找到程序的位置，再通过父子节点过滤找到程序图标，这样后期可维护性更强       
            i1="//*[contains(@text,'滴哩GO')]/../../android.widget.RelativeLayout/android.widget.FrameLayout/*[contains(@text,'体验版')]/preceding-sibling::android.widget.ImageView[1]"
    #       使用UIAutomator通过同级元素定位同级元素,需要使用find_element_by_android_uiautomator方法
            i2='new UiSelector().textContains("体验版").fromParent(new UiSelector().className("android.widget.ImageView"))'
    
            self.driver.find_element_by_xpath(i1).click()
    #         driver.find_element_by_android_uiautomator(i2).click()
            time.sleep(6)
            
        except Exception as e:
            print "cannot found the element of WeiChat"

    def find_element(self,page, section, element):
        
        try:
            element_xpath=self.get_config(page, section, element)
            
            el=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath(element_xpath),message="Wait Timeout")
            #可以可以用下面的方式,By.XPATH可以切换为其他方式(presence_of_element_located只验证元素是否在DOM不判断是否显示)
            #el=WebDriverWait(self.driver,10,1).until(EC.presence_of_element_located((By.XPATH,a)),message="No Such Element")
            return el
        except Exception as e:
            self.assertEqual(1, 0, "%s Cannot found the element %s"%(e,element))
            return False


    def xpath_getAttribute(self,page, section, element,attribute):
        #attribute根据元素的的属性填写
        return self.find_element(page, section, element).get_attribute(attribute)
    
    def xpath_click(self,page, section, element):
        self.find_element(page, section, element).click()
    
    def xpath_sendkey(self,page, section, element,data):
        el=self.find_element(page, section, element,data)
        el.clear()
        el.send_keys(data)

    def xpath_is_displayed(self,page, section, element):
        # 判断元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回元素
        # 元素显示时返回TRUE,否则False
        a=self.get_config(page, section, element)  
        try:
            el=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,a)),message="No Such Element").is_displayed()
            return el
        except:
            return False
 
    def xpath_is_existed(self,page, section, element):
        # 判断元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回元素
        # 元素存在时(不一定可见)返回元素，返回否则报错
        a=self.get_config(page, section, element)  
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,a)),message="No Such Element")
            return True
        except:
            return False

    def xpath_is_enabled(self,page, section, element):
        # 判断元素是否可用,如果是返回TRUE,不是返回False
        a=self.get_config(page, section, element)  
        try:
            el=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,a)),message="No Such Element").is_enabled()
            return el
        except:
            return False
        
    
    def xpath_is_visible(self,page, section, element):
        # 判断元素是否可见，如果可见就返回这个元素,否则报错
        #visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        #visibility_of :跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
        #WebDriverWait(test,3).until(EC.visibility_of_element_located((By.XPATH,a)))
        a=self.get_config(page, section, element)  
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element(by=By.XPATH,value=a)),message="No Such Element")
            return True
        except:
            return False

    # 判断元素的value属性是否包含指定字符串,包含返回TRUE,不包含会报错

    def Input_WeiPay(self):

        try:
        #     driver.tap([(162,1185),(206,1160),(206,1160)],1000)
        #     time.sleep(1)
        #     driver.tap([(916,1399),(162,1185),(900,1186)],1000)
            self.find_element('confirmOder','leaderGroup', 'PayBox')
            
            self.driver.tap([(162,1185)],500)
            self.driver.tap([(206,1567)],500)
            self.driver.tap([(526,1733)],500)
            self.driver.tap([(916,1399)],500)
            self.driver.tap([(162,1185)],500)
            self.driver.tap([(900,1186)],500)
           
            self.find_element('confirmOder','leaderGroup', 'SuccessPay')
            
        except Exception as e:
            print e
            return False       

    def Choose_PickUpAddress(self,page, section, element,address):
 
        try:
            el=self.find_element(page, section, element)
            el.click()
    
            el=self.find_element(page, section, address)
            el.click()
            
            return True
            
        except Exception as e:
            self.assertEqual(1, 0, "Cannot found the element %s %s"%(element,address))
            return False
    
    
    def Choose_PickUpTime(self):
        self.driver.quit()
    
    def hide_keyboard(self):
        time.sleep(3)
        self.driver.hide_keyboard()
    
    def back(self):
        self.driver.back()
    
    def qiut(self):
        self.driver.quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def Creat_leaderGroup(self):
        url = 'http://fresh.nong12.com/login/login.action'
        d='name=科学城1213团长团2人001&icon=dili-fresh/groupbuy/ecefdbfe68c14aa9b18b42a8b58b6abe&iconFile=&type=leaderGroupBuy&timeSt=2018-12-13 18:07:09&timeEnd=2018-12-31 10:44:26&deliveryTimeSt=2018-12-13 18:07:10&deliveryTimeEnd=2018-12-31 10:44:29&cityId=510100&validTime=2&limitTimes=10&groupSize=2&limitNum=2&maximumGroup=2&chairmanPrice=0.01&price=0.02&product=[{"available":100,"name":"西瓜","price":9900,"productCode":"PD2018121000000003","productId":54,"quantity":1000}]&shops=40,33&rule=<p><br></p>'
    
        header = {
            "Host": "campaign.fresh.nong12.com:8083",
            "Content-Type": "application/x-www-form-urlencoded",
            "Connection": "keep-alive",
            "Content-Length":"508",
            "Upgrade-Insecure-Requests":"1",
            "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Origin": "http://campaign.fresh.nong12.com:8083",
            "Cache-Control": "max-age=0",
            "Referer": " http://campaign.fresh.nong12.com:8083/campaign/copy.html?id=441",
            "Cookie": "u=260; n=admin; userId=26; username=lixi; loginPath=http://fresh.nong12.com/login/index.html; SessionId=7b89cdf2-7207-43ee-8cf9-ad92c643f010",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"
        
        }
        
        
        header_str=json.dumps(header)
        header_dict=json.loads(header_str)
        
        #data必须位str，headers必须位dict
        r = requests.post(url, data=d,headers=header_dict)
        
        
        print r.status_code
        
    
    
    
    

    def set_priority(self,value):
        global _global_priority
        _global_priority=value
        
        return _global_priority
    
    def read_priority(self):
        return _global_priority
    
    def _p(self,_value):
            if _global_priority == 1:
                return False
            elif _global_priority == 2:
                if _value == 1:
                    return True
                else:
                    return False
            elif _global_priority == 3:
                if _value == 3:
                    return False
                else :
                    return True
            else:
                raise ValueError