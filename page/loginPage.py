from base.base import Base
import page
from time import sleep


class LoginPage(Base):
    """登陆页面"""
    def email_element(self):
        """邮箱地址"""
        return self.base_find(page.clac_login_email)

    def password_element(self):
        """密码"""
        # print(page.clac_menu)
        # print(page.clac_login_email)
        return self.base_find(page.clac_login_password)

    def login_button(self):
        """登陆按钮"""
        return self.base_find(page.clac_login_button)

    def email_error_element(self):
        """邮箱地址错误"""
        return self.base_find(page.clac_login_error_email)

    def password_error_element(self):
        """密码错误"""
        return self.base_find(page.clac_login_error_password)

    def login_fail_element(self):
        """登陆失败"""
        return self.base_switch_alert()

    def login(self, email=page.email, password=page.password):
        """登陆操作"""
        self.email_element().send_keys(email)
        self.password_element().send_keys(password)
        self.login_button().click()

    def login_test(self, driver, email, password):
        """测试登录页面"""
        self.email_element().clear()
        self.password_element().clear()
        sleep(2)
        if email != None:
            self.email_element().clear()
            self.email_element().send_keys(email)
        if password != None:
            self.password_element().clear()
            self.password_element().send_keys(password)
        # if password == None:
        #     print("wefvgdgwerasfgbnhtjmyiutygredwqrgethjmhgrfdws")
        #     self.email_element().clear()
        #     self.password_element().clear()
        #     self.email_element().send_keys(" ")
        #     self.login_button().click()
        #     sleep(5)
        #     self.email_element().clear()
        #     self.password_element().clear()
        #     self.email_element().send_keys(email)
        #     self.password_element().clear()
        #     alert = driver.switch_to_alert()
        #     alert.accept()
        #     self.password_element().clear()
        #     sleep(5)
        sleep(1)
        self.login_button().click()


if __name__ == "__main__":
    from base.get_driver import GetDriver
    driver = GetDriver.get_driver()
    a = LoginPage(driver)
    a.login()
    alert = driver.switch_to_alert()
    print(alert.text)
    print(12)

