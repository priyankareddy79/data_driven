import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")

def Login_Loginout_Setup():
    driver = webdriver.Chrome(executable_path=r"C:\Users\priyanka\Desktop\chromedriver-win64\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver

    time.sleep(10)
    driver.find_element_by_xpath("//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
    driver.close()