import os
import unittest
import time
from appium import webdriver
from subprocess import Popen
from Page.basic_page import *


class basic_unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("--------------Test Start--------------")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '6.0.1'  # 手机版本
        desired_caps['deviceName'] = 'd2acaa52'  # 设备名称
        # desired_caps['platformVersion'] = '25'
        desired_caps['appPackage'] = 'com.enhance.kaomanfen.yasilisteningapp'
        desired_caps['appActivity'] = 'com.enhance.kaomanfen.yasilisteningapp.activity.AppStartActivity'
        desired_caps['noReset'] = True
        desired_caps['autoLaunch'] = False
        # desired_caps['automationName'] = "UiAutomator2"
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # cls.driver.find_element_by_accessibility_id()


    @classmethod
    def tearDownClass(cls):
        print("--------------Test End--------------")
        time.sleep(3)
        cls.driver.quit()

