from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Login:
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(1)
        listOfProducts = driver.find_elements(By.CLASS_NAME,"inventory_item")
        testResult = len(listOfProducts) == 6
        print(len(listOfProducts))
      


testClass = Test_Login()
testClass.test_valid_login()