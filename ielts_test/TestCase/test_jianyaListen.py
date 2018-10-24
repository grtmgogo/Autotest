#coding=utf-8
from time import sleep
from Page.basic_page import *
from Page.Login_Page import Login_page
from TestCase.basic_unittest import *
import unittest
from selenium.webdriver.common.by import By


class JianyaListenTest(basic_unittest):
    def setUp(self):
        self.driver.launch_app()

    def test_jianyaListen(self):
        base = Basic_page(self.driver)
        sleep(10)
        base.swipe_up()
        sleep(1)
        base.click(By.ID, 'com.enhance.kaomanfen.yasilisteningapp:id/ll_jianya_listen')
        # 用text属性定位
        self.driver.find_element_by_android_uiautomator('text(\"剑桥雅思听力7\")').click()
        self.driver.find_element_by_android_uiautomator('text(\"全部下载\")').click()
        sleep(5)

        list = []
        list.append(self.driver.find_element_by_android_uiautomator('index(2)'))
        print("下载按钮是" + str(len(list)) + "个")

        while True:
            if len(list) == 1:
                print("Section个数" + str(len(self.driver.find_elements_by_android_uiautomator('text(\"Section 1\")'))))
                self.driver.find_elements_by_android_uiautomator('text(\"Section 1\")')[0].click()
                break
            list = []
            list.append(self.driver.find_element_by_android_uiautomator('index(2)'))
            sleep(1)
        self.driver.press_keycode(4)
        self.driver.press_keycode(3)
        sleep(20)

    def tearDown(self):
        self.driver.close_app()

if __name__ =="__main__":
    testsuit = unittest.TestSuite()
    testsuit.addTest(JianyaListenTest("test_jianyaListen"))
    # testsuit.addTest(ListenVocTest("test_login2"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)


