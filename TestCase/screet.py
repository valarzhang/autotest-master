# coding: utf-8

import unittest, random, os, traceback,time
from selenium import webdriver
from BeautifulReport import BeautifulReport

SCREENSHOT_DIR = './test_result'


# class Test1(unittest.TestCase):
#     def setUp(self):
#         self.dr = webdriver.Chrome()
#         dr=self.dr
#         print('登录统一开发平台')
#         dr.get("https://www.baidu.com/")  # 打开统一平台地址
#         dr.maximize_window()  # 将浏览器最大化
#
#         # 重新赋值failureException，注意：failureException的值是一个类，不是类实例
#         self.failureException = self.failure_monitor()
#
#     def failure_monitor(self):
#         test_case = self  # 将self赋值给test_case，以便下方的AssertionErrorPlus内部类可调用外部类的方法
#
#         class AssertionErrorPlus(AssertionError):
#             def __init__(self, msg):
#                 try:
#                     cur_method = test_case._testMethodName  # 当前test函数的名称
#                     unique_code = ''.join(random.sample('1234567890', 5))  # 随机生成一个值，以便区分同一个test函数内不同的截图
#                     file_name = '%s_%s.png' % (cur_method, unique_code)
#                     test_case.dr.get_screenshot_as_file(os.path.join(SCREENSHOT_DIR, file_name))  # 截图生成png文件
#                     print('失败截图已保存到: %s' % file_name)
#                     msg += '\n失败截图文件: %s' % file_name
#                 except BaseException:
#                     print('截图失败: %s' % traceback.format_exc())
#
#                 super(AssertionErrorPlus, self).__init__(msg)
#
#         return AssertionErrorPlus  # 返回AssertionErrorPlus类
#
#     def test1(self):
#         self.assertEqual(0, 1, '错误提示')
#
#     def test2(self):
#         self.assertEqual(1,1)
#
#     def test3(self):
#         self.assertEqual(1,2)


class Test2(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        dr = self.dr
        print('登录统一开发平台')
        dr.get("https://www.baidu.com/")  # 打开统一平台地址
        dr.maximize_window()  # 将浏览器最大化


    def save_img(self,img_name):
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))
        #os.path.abspath(r"G:\Test_Project\img")截图存放路径

    def tearDown(self):
        self.dr.close()

    @BeautifulReport.add_test_img('Test2_test_1')
    def test_1(self):
        dr = self.dr
        dr.find_element_by_id("kw").send_keys("selenium")
        time.sleep(1)
        self.save_img('Test2_test_1')
        dr.find_element_by_id("123").click()
        time.sleep(1)
        # dr.find_element_by_link_text("MeterSphere - 开源持续测试平台").click()
        # self.save_img('Test2_test_1')
        # self.assertEqual(1,2)


if __name__ == "__main__":
    unittest.main()
