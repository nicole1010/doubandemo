

from initialization import browserdriver

class BasePageObject():

    def __init__(self):
        self.driver = browserdriver.build_up_driver()

    def extend_find_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].style.background "
                                   "= 'rgb(138,43,226 )';",
                                   element)
        return element

    def switch_frame_by_element(self, element):
        self.driver.switch_to.frame(element)

    def switch_frame_by_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def get_element_text(self, element):
        return element.text

    def get_table_content(self, tabel_name):
        pass

    def set_value(self, element, value):
        element.clear()
        element.click()
        element.send_keys(value)

    def click_element(self, element):
        element.click()

    def set_book_value(self, element, value):
        # set_book_value 不需要clear方法，输入框没有记录上一次输入的内容
        # element.clear()
        element.click()
        element.send_keys(value)





