import pytest
from pages.bookpage import BookPageObject


# todo teardown 关闭浏览器
# todo 增加一个driver处理，handles-每次都只使用当前浏览器，不打开新的浏览器

class TestDoubanBook(object):

    @classmethod
    def setup_class(cls):
        cls._query_book = BookPageObject()

    @classmethod
    def teardown_class(cls):
        cls._query_book.driver.quit()


    # @pytest.mark.parametrize('queryname',[
    #     ('利用Python进行数据分析')
    # ])
    def test_read_book(self):
        queryname = '利用Python进行数据分析'
        self._query_book.querybook(queryname)
        assert self._query_book.get_my_book_text() == '利用Python进行数据分析'  #书名判断

    def test_read_author(self):
        queryname = '利用Python进行数据分析'
        self._query_book.querybook(queryname)

        if "Wes McKinney" in str(self._query_book.driver.page_source):       #作者判断
            assert True
        else:
            assert False








