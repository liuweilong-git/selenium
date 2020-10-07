import unittest
import time
from page.aboutPage import AboutPage
from base.get_driver import GetDriver


class TestAbout(unittest.TestCase):
    """测试关于我们页面"""
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver.get_driver()
        cls.about = AboutPage(cls.driver)
        cls.about.login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    def test_about01(self):
        """进入关于我们页面测试"""
        self.about.about_menu("关于我们")
        time.sleep(2)
        about = self.about.about_element()
        self.assertEqual("关于我们", about.text)


if __name__ == '__main__':
    unittest.main()
