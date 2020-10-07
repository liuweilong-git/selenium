from selenium.webdriver.common.by import By
from base.base import Base
from page.loginPage import LoginPage
import page


class AboutPage(LoginPage):
    """关于我们页面"""
    def about_menu(self, menu):
        return self.base_select_menu(menu)
    
    def about_element(self):
        """关于我们页面判断元素"""
        return self.base_find(page.clac_about)
