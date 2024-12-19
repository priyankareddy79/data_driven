class class_Login_page:
    def __init__(self,driver):
        self.driver = driver

    def username(self,usn):
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(usn)

    def password(self,pd):
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(pd)

    def Login(self):
        self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()