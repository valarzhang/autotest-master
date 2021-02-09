import unittest,time
from BeautifulReport import BeautifulReport



if __name__ == '__main__':
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    file_name =  '统一开发平台测试报告'+ now_time + '.html'
    suite_tests = unittest.defaultTestLoader.discover("./TestCase", pattern="test_*.py", top_level_dir=None)
    BeautifulReport(suite_tests).report(filename=file_name, description='统一开发平台', report_dir='./test_result')