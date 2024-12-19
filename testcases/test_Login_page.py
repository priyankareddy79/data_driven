import time
import pytest
import openpyxl
from Source.login_page import class_Login_page
from datetime import datetime


#Function to read data from EXCel file.

def Read_test_data():
    #code to load the data from excel file
    workbook = openpyxl.load_workbook(filename=r"C:\Users\priyanka\PycharmProjects\Data_Driven_Framework\Data\Data_driven_login_2.xlsx")
    sheet = workbook["Sheet1"]
    data_list =[] #creating empty list to add every row of excel file data as tuple(row).

    #adding data to data_list from excel file.
    for row in sheet.iter_rows(min_row=2,values_only=True):
        user, pwd, result = row
        #here two brackets using one is appened() method,2nd bracket if for tuple.
        data_list.append((user, pwd, result))
    return data_list

#calling function (test data is a object of read_test_data function)
test_data = Read_test_data()
#parameterize the testt function with data from the excel file.
@pytest.mark.parametrize("username,password,expresult",test_data)

def test_login(username,password,expresult,Login_Loginout_Setup):
    #this is conftest file method to open  browseer, and display login page.
    driver = Login_Loginout_Setup

    #creating a object (login_page) for LOgin_page class of source package
    #this class_login_page class will find username, password and login button elements locators.
    login_page = class_Login_page(driver)
    time.sleep(5)

    login_page.username(username)
    login_page.password(password)

    login_page.Login()

    if expresult == "pass":
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\Users\\priyanka\\PycharmProjects\\Data_Driven_Framework\\screenshots\\Login_success_{dt}.png")
        time.sleep(5)
        print(f"login test with username'{username}' and password '{password} Test passed! ")

    else:
        dt = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        time.sleep(5)
        driver.save_screenshot(f"C:\\Users\\priyanka\\PycharmProjects\\Data_Driven_Framework\\screenshots\\Login_failed_{dt}.png")
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/"
        print(f"login test with username '{username}' and password '{password} Testfailed!")