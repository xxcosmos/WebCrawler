# -*- coding: utf-8 -*-

# 导入 web 驱动包
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class taobao_info:

    def __init__(self):
        self.url = 'https://login.taobao.com/member/login.jhtml'

        options = webdriver.ChromeOptions()

        # 不加载图片，加快访问速度
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

        # 设置为开发者模式
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)

        # 设置超时时间
        self.wait_time = WebDriverWait(self.browser, 10)

    def login(self, weibo_username, weibo_password):
        # 打开网页
        self.browser.get(self.url)

        # 等待密码登录出现
        password_login = self.wait_time.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()

        alipay_login = self.wait_time.until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.alipay-login')))
        alipay_login.click()


        username = self.wait_time.until(expected_conditions.presence_of_element_located((By.ID, 'J-input-user')))
        username.send_keys(weibo_username)

        pwd = self.wait_time.until(expected_conditions.presence_of_element_located((By.ID, 'password_rsainput')))
        pwd.send_keys(weibo_password)

        submit = self.wait_time.until(
            expected_conditions.presence_of_element_located((By.ID, 'J-login-btn')))
        submit.click()

        taobao_name = self.wait_time.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            '.site-nav-bd > '
                                                                                            'ul.site-nav-bd-l > '
                                                                                            'li#J_SiteNavLogin > '
                                                                                            'div.site-nav-menu-hd > '
                                                                                            'div.site-nav-user > '
                                                                                            'a.site-nav-login-info'
                                                                                            '-nick ')))
        print(taobao_name)


if __name__ == '__main__':
    weibo_username = 'xxxx'
    weibo_password = 'xxx.'

    a = taobao_info()
    a.login(weibo_username, weibo_password)
