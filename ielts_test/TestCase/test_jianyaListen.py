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
        sleep(10)
        base.click(By.ID, 'com.enhance.kaomanfen.yasilisteningapp:id/ll_jianya_listen')
        # 用text属性定位
        self.driver.find_element_by_android_uiautomator("剑桥雅思听力4").click()

    def tearDown(self):
        self.driver.close_app()

if __name__ =="__main__":
    testsuit = unittest.TestSuite()
    testsuit.addTest(JianyaListenTest("test_jianyaListen"))
    # testsuit.addTest(ListenVocTest("test_login2"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)


