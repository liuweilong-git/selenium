from selenium import webdriver
import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    GetDriver.get_driver()