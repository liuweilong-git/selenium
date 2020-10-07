from selenium.webdriver.common.by import By
"""以下为服务器域名配置地址"""
url = "http://172.27.37.158:9536/#/"  # 每次都需要修改

# 默认的邮箱与地址
email = "admin@tynam.com"
password = "tynam123"

"""关于页面元素的配置"""
# 关于我们
clac_about = By.CSS_SELECTOR, "#about h1"

# 关于登录页面
clac_login_email = By.CLASS_NAME, "email"
clac_login_password = By.CLASS_NAME, "password"
clac_login_button = By.CSS_SELECTOR, ".login-btn>input[value='登  录']"
clac_login_error_email = By.CSS_SELECTOR, ".email+div.msg"
clac_login_error_password = By.CSS_SELECTOR, ".password+div.msg"

# 关于菜单：
clac_menu = By.CSS_SELECTOR, '#menu>div>h4'

# 关于Home
calc_home_input = By.ID, "search-input"
calc_home_search = By.CLASS_NAME, "search"
calc_home_add = By.ID, "add"
calc_home_edt = By.ID, "edt"
calc_home_del = By.ID, "del"
calc_home_add_code = By.CSS_SELECTOR, "#add-dialog .code"
calc_home_add_name = By.CSS_SELECTOR, "#add-dialog .name"
calc_home_add_sex = By.CSS_SELECTOR, "#add-dialog .sex"
calc_home_add_grader = By.CSS_SELECTOR, "#add-dialog .grader"
calc_home_add_confirm = By.CSS_SELECTOR, "#add-dialog #confirm"
calc_home_add_cancel = By.CSS_SELECTOR, "#add-dialog #cancel"
calc_home_del_confirm = By.CSS_SELECTOR, "#del-dialog #confirm"
calc_home_del_cancel = By.CSS_SELECTOR, "#del-dialog #cancel"