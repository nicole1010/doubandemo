
from pages.basepage import BasePageObject
from selenium.webdriver.common.by import By
import time


class BookPageObject(BasePageObject):
    # 未登录时，定位读书按钮
    _locate_ink_book = (By.LINK_TEXT, '豆瓣读书')
    # 登录时，定位读书按钮
    # _douban_tab = (By.LINK_TEXT,"读书")

    _locate_input_field = (By.ID, 'inp-query')
    _sumbit_query = (By.CLASS_NAME, 'inp-btn')  #找父节点

    _locate_bookname = (By.LINK_TEXT, '利用Python进行数据分析')

    def __init__(self):
        BasePageObject.__init__(self)

    def _locate_read_tab(self):
        return self.extend_find_element(BookPageObject._locate_ink_book)

    def click_read_tab(self):
        self.click_element(self._locate_read_tab())

    def _locate_inputquery_field(self):
        return self.extend_find_element(BookPageObject._locate_input_field)

    def input_read_query(self, query_name):
        # set_book_value 不需要clear方法，输入框没有记录上一次输入的内容
        self.set_book_value(self._locate_inputquery_field(), query_name)

    def _locate_sumbit(self):
        return self.extend_find_element(BookPageObject._sumbit_query)

    def click_submit(self):
        self.click_element(self._locate_sumbit())

    def _find_my_book(self):
        return self.extend_find_element(BookPageObject._locate_bookname)

    def get_my_book_text(self):
        return self.get_element_text(self._find_my_book())

    def querybook(self, queryname):
        # 未登录状态，点击读书按钮<---当前登录时总需要滑动验证
        self.click_read_tab()

        #豆瓣找不着windowname，尝试很多网站window.name其实都是""。明天找前端大佬问问

        # 切换页面，方法一--助教教的方法
        # 切换到倒数第一个页面，因为倒数第一个就是豆瓣读书页面
        # window_handles_list= self.driver.window_handles
        # print(window_handles_list)
        # self.switch_frame_by_window(window_handles_list[-1])
        # time.sleep(3)
        # print(self.driver.current_window_handle )
        # if self.driver.current_window_handle == window_handles_list[-1]:
        #     print("切换窗体成功")

        # 切换页面，方法二
        # 当前所有页面的title值 == 豆瓣读书页面的title ,留在这个窗体呆着
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            # 打印当前所有页面的title, 方便找出豆瓣读书页面的title作为下面的判断值
            # print(self.driver.title)
            if self.driver.title == '豆瓣读书':
                break
        # 输入查询词
        self.input_read_query(queryname)
        # 点击查询按钮
        self.click_submit()









