from selenium import webdriver
from selenium.webdriver.common.by import By
from webium import BasePage, Find
import time

class MoviePageObject():
    _movie_query = (By.ID, "inp-query")
    _kongbu_movie_query = (By.ID, "kongbu-query")
    _movie_search_icon = (By.CLASS_NAME, "inp-btn")

    def __init__(self):   #不写也是默认 pass 的状态
        pass

    def _locate_movie_query(self):
        pass

    def input_movie_query_name(self, name):
        pass

    # def locate_kongbu_movie_query(self):
    #     pass
    #
    # def input_kongbu_movie_query(self, name):
    #     pass

    def _locate_search_movie_icon(self):
        pass

    def click_search_movie_icon(self):
        pass

    def get_search_result(self):
        pass

    def goto_main_page(self):
        pass


    




