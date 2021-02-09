# coding=utf-8
import unittest
from functools import wraps
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait


def wait_element(dr, method, attribute,timeout=10):
    """
    作者：张丽

    :param method:
       By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR
    :param attribute: 元素属性值
       例如：'android.widget.TextView'
    :param timeout:超时时间，等待的最长时间，默认为30秒
    :param poll_frequency: 查询间隔时间，默认间隔0.5秒
    :return: 返回的为元素定位

    """
    try:
        if method == 'By.ID':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_element_by_id(attribute))
        elif method == 'By.CLASS_NAME':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_element_by_class_name(attribute))
        elif method == 'By.NAME':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_element_by_name(attribute))
        elif method == 'By.XPATH':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_element_by_xpath(attribute))
        elif method == 'By.CSS_SELECTOR':
            return WebDriverWait(dr,  timeout).until(lambda x: x.find_element_by_css_selector(attribute) )
        elif method == 'By.LINK_TEXT':
            return WebDriverWait(dr,  timeout).until(lambda x: x.find_element_by_link_text(attribute) )
        else:
            return False
    except:
        return False






def wait_elements(dr, method, attribute,timeout=10):
    """
    作者：张丽

    :param method:
       By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR
    :param attribute: 元素属性值
       例如：'android.widget.TextView'
    :param timeout:超时时间，等待的最长时间，默认为30秒
    :param poll_frequency: 查询间隔时间，默认间隔0.5秒
    :return: 返回的为元素定位

    """
    try:
        if method == 'By.ID':
            return WebDriverWait(dr,timeout).until(lambda x: x.find_elements_by_id(attribute))
        elif method == 'By.CLASS_NAME':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_elements_by_class_name(attribute))
        elif method == 'By.NAME':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_elements_by_name(attribute))
        elif method == 'By.XPATH':
            return WebDriverWait(dr, timeout).until(lambda x: x.find_elements_by_xpath(attribute))
        elif method == 'By.CSS_SELECTOR':
            return WebDriverWait(dr,  timeout).until(lambda x: x.find_elements_by_css_selector(attribute) )
        elif method == 'By.LINK_TEXT':
            return WebDriverWait(dr,  timeout).until(lambda x: x.find_elements_by_link_text(attribute) )
        else:
            return False
    except:
        return False



def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):

        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)
        return inner_func
    return wraper_func





