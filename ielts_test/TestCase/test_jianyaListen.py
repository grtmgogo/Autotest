#coding=utf-8
from time import sleep
from Page.basic_page import *
from Page.Login_Page import Login_page
from TestCase.basic_unittest import *
import unittest
from selenium.webdriver.common.by import By

class ListenVocTest(basic_unittest):
    def setUp(self):
        self.driver.launch_app()

    def test_jianyaListen(self):
        base = Basic_page(self.driver)
        sleep(10)
        base.swipe_up()
        sleep(10)
        base.click(By.ID, 'com.enhance.kaomanfen.yasilisteningapp:id/ll_listen_vocabulary')

    def tearDown(self):
        self.driver.close_app()

if __name__ =="__main__":
    testsuit = unittest.TestSuite()
    testsuit.addTest(ListenVocTest("test_ListenVoc"))
    # testsuit.addTest(ListenVocTest("test_login2"))


