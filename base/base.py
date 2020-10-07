import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        # 使用显示等待查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素方法封装
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入元素方法封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息方法封装
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 截图方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png"
                                           .format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在

    def base_find_elements(self, by, selenium):
        """返回一组定位元素"""
        return self.driver.find_elements(by, selenium)

    def base_switch_alert(self):
        """返回弹窗页面"""
        return self.driver.switch_to.alert()

    def base_select_menu(self, menu_text):
        """菜单选择"""
        menus_element = self.base_find_elements(By.CSS_SELECTOR, "#menu>div>h4")
        for menu in menus_element:
            # replace(" ", "")去掉字符串中的空格
            if menu.text.replace(" ", "") == menu_text.replace(" ", ""):
                return menu.click()
        print(menu_text + "未找到")
        return

    def log_out(self):
        """退出登陆"""
        return self.base_select_menu("退出登录")
