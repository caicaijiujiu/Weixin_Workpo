from selenium.webdriver.chrome.webdriver import WebDriver

from test_weixinwork.base_page import Base_Page


class Register(Base_Page):

    # def __init__(self,driver:WebDriver):
    #     #上面导入时选择第一个中的remote的webdriver   driver:WebDriver中加了WebDriver 下面就可以直接点出来方法了 python3.7之后的功能
    #     self.driver = driver

    def register(self):
        self.find('//*[@id="corp_name"]').send_keys('菜菜九九')
        self.find('//*[@id="corp_industry"]/a').click()
        self.find('//*[@id="corp_industry"]/div/table/tbody/tr/td[1]/div[14]').click()
        self.find('//*[@id="corp_industry"]/div/table/tbody/tr/td[2]/div[14]/div[4]/a').click()
        # tags[14].click()
        # for tag in tags:
        #     if tag.text == '生活服务':
        #         tag.click()
        #         self.driver.find_element_by_xpath('//*[@id="corp_industry"]/a/span[1]').click()
        return True