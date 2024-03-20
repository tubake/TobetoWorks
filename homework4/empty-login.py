from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Test_Login:
    def test_empty_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys()
        passwordInput.send_keys()
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        #print(errorMessage.text)
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")



testClass = Test_Login()
testClass.test_empty_login()

#succesfull  