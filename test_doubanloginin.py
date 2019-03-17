import pytest
from selenium import webdriver


def douban(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(6)
    self.driver.get("https://www.douban.com")
    login_iframe = self.driver.find_element_by_tag_name('iframe')
    self.driver.switch_to.frame(login_iframe)
    self.driver.find_element_by_class_name('account-tab-account').click()
    self.driver.find_element_by_id('username').send_keys('nicocui@163.com')
    self.driver.find_element_by_name('password').send_keys('douban@nicole01')
    self.driver.find_element_by_link_text('登录豆瓣').click()
    elements = self.driver.find_elements_by_link_text("我的豆瓣")
    # assert len(elements) > 0
    # page = self.driver.page_source
    # assert  '说句话' in page