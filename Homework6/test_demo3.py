from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 
import pytest
import openpyxl
from constants.globalConstants import *
import json


class Test_Demo:

    #pytest tarafından tanımlanan bir method 
    #her test öncesi otomatik olarak çalıştırılır
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    #her test bitiminde çalışacak fonk
    def teardown_method(self):
        self.driver.quit()



    def getDataFromjson():
        with open("data.json", "r+", encoding="utf-8") as json_file:
            data = json.load(json_file)
            invalid_users = data.get('login_info',  [])
            return [(user.get('username'),user.get('password')) for user in invalid_users]




    
    @pytest.mark.parametrize("username,password",getDataFromjson("data/data.json"))
    def test_invalid_login(self,username,password):
        userNameInput = self.waitForElementVisible((By.ID,username_id))
        passwordInput = self.waitForElementVisible((By.ID,password_id))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = self.waitForElementVisible((By.ID,login_button_id))
        loginButton.click()
        errorMessage = self.waitForElementVisible((By.ID,errorMessage_xpath))
        assert errorMessage.text == errorMessage_text

    def test_valid_login(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,username_id)))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,password_id)))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() 
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,login_button_id)))
        loginButton.click()
        baslik = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,title_xpath)))
        assert baslik.text == title_text
        
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))