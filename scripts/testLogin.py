import unittest
import page
import time
from page.loginPage import LoginPage
from parameterized import parameterized
from base.get_driver import GetDriver
from base.ExcelUtil import ExcelUtil


def get_data():
    """
    获取数据
    得到有用的数据，并且使数据以邮箱地址，密码，预期结果定位，预期结果的顺序返回
    :return:
    """
    # 获得Excel中的文件数据
    sheet = "Login"
    file = ExcelUtil(sheet_name=sheet)
    data = file.get_data()

    # 得到所需要数据的索引，然后根据索引获取相应顺序的数据
    email_index = data[0].index("邮箱地址")
    password_index = data[0].index("密码")
    expected_element_index = data[0].index("预期结果定位")
    expected_index = data[0].index("预期结果")

    data_length = data.__len__()
    all_case = []
    # 去除header行，和其他无用的数据
    for i in range(1, data_length):
        case = []
        case.append(data[i][email_index])
        case.append(data[i][password_index])
        case.append(data[i][expected_element_index])
        case.append(data[i][expected_index])
        all_case.append(case)
    return all_case


def login_assert(driver, calc, assert_type, assert_message):
    # 登录断言
    if assert_type == "email error":
        email_message = calc.email_error_element().text
        # print(email_message, assert_message)
        assert email_message == assert_message
    elif assert_type == "password error":
        password_message = calc.password_error_element().text
        # print(password_message, assert_message)
        assert password_message == assert_message
    elif assert_type == "login fail":
        alert = driver.switch_to_alert()
        login_message = alert.text
        alert.accept()
        time.sleep(1)
        assert login_message == assert_message
    else:
        print("输入的断言类型不正确")


class TestLogin(unittest.TestCase):
    # 登录测试
    driver = None

    @classmethod
    def setUpClass(cls):#(self):#Class(cls):
        cls.driver = GetDriver.get_driver()
        cls.calc = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):#(self):#Class(cls) -> None:
        GetDriver().quit_driver()

    # 测试
    @parameterized.expand(get_data())
    def test_login01(self, email, password, assert_type, expect):
        # 登录成功
        self.calc.login_test(self.driver, email, password)
        if expect == "登录成功":
            time.sleep(5)
            self.calc.log_out().click()
            time.sleep(5)
            try:
                login_assert(self.driver, self.calc, assert_type, expect)
            except:
                # 截图
                self.calc.base_get_image()
        else:
            try:
                login_assert(self.driver, self.calc, assert_type, expect)
            except:
                # 截图
                self.calc.base_get_image()


if __name__ == '__main__':
    unittest.main()

