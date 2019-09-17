# 导入 web 驱动
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class taobao_info:

    def __init__(self):
        self.url = 'https://login.taobao.com/member/login.jhtml'

        options = webdriver.ChromeOptions()

        # 不加载图片，加快访问速度
        options.add_experimental_option("prefs",{"profile.managed_default_content_settings.images":2})

        # 设置为开发者模式
        options.add_experimental_option('excludeSwitches',['enable-automation'])

        self.browser = webdriver.Chrome(executable_path='/Applications/Google Chrome.app',options=options)

        # 设置超时时间
        self.wait_time = WebDriverWait(self.browser,10)

    def login(self):
        self.browser.get(self.url)

        self.wait_time.until(expected_conditions.presence_of_element_located())
