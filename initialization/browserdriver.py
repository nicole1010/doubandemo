
from selenium import webdriver




def build_up_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--handles')   # 只使用当前浏览器，不打开新浏览器，生效后需要换成close关闭页面
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.get("https://www.douban.com/")
    return driver