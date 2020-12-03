from selenium.webdriver.remote.webdriver import WebDriver

from test_weixinwork import index
from test_weixinwork.register import Register


class login:
    """
    登录po
    """

    def __init__(self,driver:WebDriver):
        #上面导入时选择第一个中的remote的webdriver   driver:WebDriver中加了WebDriver 下面就可以直接点出来方法了 python3.7之后的功能
        self.driver = driver


    def scan(self):
        pass

    def goto_register(self):
        self._driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)