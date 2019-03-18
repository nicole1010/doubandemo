import pytest
from pages.bookpage import BookPageObject
from selenium import webdriver


# todo teardown 关闭浏览器
# todo 增加一个driver处理，handles-每次都只使用当前浏览器，不打开新的浏览器


# 切换 window 时，没有windowname时，哪种方法合适，目前有三种思路：
# 助教给的思路，找到当前倒数第一个window
# 查资料找到的思路，变量当前所有window title ,找到当前 window 时break
# 进入 window 时，给 window 赋一个window.name --> 还没有尝试，跟前端同事沟通时想出的一个方法
# 还有更好的方式吗？

class TestDoubanBook(object):

    _query_book = None

    @classmethod
    def setup_class(cls):
        cls._query_book = BookPageObject()

    @classmethod
    def teardown_class(cls):
        cls._query_book.driver.quit()


    @pytest.mark.parametrize('queryname', [
        ('利用Python进行数据分析')
    ])
    def test_read_book(self, queryname):
        self._query_book.querybook(queryname)
        assert self._query_book.get_my_book_text() == '利用Python进行数据分析'  #书名判断


    @pytest.mark.parametrize('queryname', [
        ('利用Python进行数据分析')
    ])
    def test_read_author(self, queryname):
        self._query_book.querybook(queryname)
        assert "Wes McKinney" in str(self._query_book.driver.page_source)

        # if "Wes McKinney" in str(self._query_book.driver.page_source):       #作者判断
        #     assert True
        # else:
        #     assert False








