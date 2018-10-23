import os,unittest,time
# from Report.HTMLTestRunner3 import HTMLTestRunner
from HTMLTestRunner.BSTestRunner import BSTestRunner
import sys

def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    # test_dir = os.getcwd()+'\\TestCase\\'
    test_dir = os.path.realpath('TestCase')

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test_*.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():
    now = time.strftime("%Y-%m-%d_%H%M%S")
    # report_name = os.getcwd()+'\\Report\\result.html'
    report_name = os.path.join(os.path.realpath("Report"), (now + '_result.html'))
    return report_name


if __name__ == '__main__':

    TestSuite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(TestSuite)

    # with open(report(),'wb') as fp:
    #     runner = BSTestRunner(stream=fp,title='Test Report',description='Test case result')
    #     runner.run(TestSuite)