import unittest
from time import sleep
from page.loginPage import LoginPage
from base.get_driver import GetDriver


class TestLogout(unittest.TestCase):
    """测试退出登录功能"""
    driver = None

    @classmethod
    def setUpClass(cls):  # (self):#Class(cls):
        cls.driver = GetDriver.get_driver()
        cls.calc = LoginPage(cls.driver)
        cls.calc.login()

    @classmethod
    def tearDownClass(cls):  # (self):#Class(cls) -> None:
        GetDriver().quit_driver()

    def test_logout01(self):
        """测试退出登录"""
        self.calc.log_out()


if __name__ == '__main__':
    unittest.main()
