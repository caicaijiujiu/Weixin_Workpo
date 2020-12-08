from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page:
    _driver = None
    _base_url = ""
    #加_表示自有变量


    #现在这个类是父类，如果子类中声明了一个init，会覆盖掉父类的init
    def __init__(self,driver:WebDriver = None):

        if driver is None:

            #初始化driver
            chrome_options = Options()
            chrome_options.debugger_address = '127.0.0.1:9222'
            #cmd中要先启动chrom浏览器 chrome --remote-debugging-port=9222，否则调不起来这里
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        if self._base_url != "":
            #访问url（Index）中的
            self._driver.get(self._base_url)

    def find(self,locator):
        return self._driver.find_element_by_xpath(locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def wait_for_click(self,locator):#显示等待   可以重写显示等待：频繁的去点击，直到找到某个元素
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self,condition):#显示等待   可以重写显示等待：频繁的去点击，直到找到某个元素
        WebDriverWait(self._driver,10).until(condition)