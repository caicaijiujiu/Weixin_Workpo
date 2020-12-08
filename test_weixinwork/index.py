from time import sleep

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_weixinwork.base_page import Base_Page
from test_weixinwork.login import login
from test_weixinwork.register import Register


class Index(Base_Page):
    _base_url = "https://work.weixin.qq.com/"
    #https://work.weixin.qq.com/  如果页面已经打开了，这里就没用了，如果页面没有打开就会调这个地址
    # def __init__(self):
    #     pass
        # chrome_options = Options()
        # chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)


        # self.driver = webdriver.Chrome()
        # self.driver.get('https://work.weixin.qq.com/')
        # 可以不写路径了，环境变量加了  'D:\Python38\chromedriver.exe'


    def goto_register(self):

        #点击立即注册
        #进入到立即注册的po
        # self.driver.get('https://work.weixin.qq.com/')
        #self.find('//*[@id="tmp"]/div[1]/a').click()
        #return Register(self._driver)#self._de????

        def add_name_click_enable():
            elements_len = len(self.finds(By.ID,"corp_name"))
            if elements_len <= 0:
                self.find('//*[@id="tmp"]/div[1]/a').click()
            return elements_len > 0
        self.wait_for_condition(add_name_click_enable)
        return Register(self._driver)
       #显示等待   ----------------------------------------------------
        # def corp_name_click_enable():
        #     length = len(self.finds(By.ID,"corp_name"))
        #     if length <= 0:
        #         self.find('//*[@id="tmp"]/div[1]/a').click()
        #     return length > 0
        #
        # self.wait_for_condition(corp_name_click_enable)
        #
        # return Register(self._driver)#self._de????

       # 显示等待   ----------------------------------------------------

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录的po
        """
        # self.driver.get('https://work.weixin.qq.com/')
        self.find('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return login(self._driver)


        pass

# gg = Index()
# gg.goto_register()