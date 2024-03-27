from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_Login:
    def setup_method(self):#her testen önce çağrılır.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self):
        self.driver.quit() 


    @pytest.mark.parametrize("username,password",[("1","secret_sauce"),("standard_user","1"),("1","1")])
    def test_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_valid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        products=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"inventory_item_description")))
         
    @pytest.mark.parametrize("username,password",[("","")])
    def test_empty_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,'user-name')
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput)
        actions.send_keys_to_element(passwordInput)
        loginButton = self.driver.find_element(By.ID,'login-button')
        loginButton.click()
        errormessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errormessage.text == "Epic sadface: Username and password are required"    
    

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput)
        actions.send_keys_to_element(passwordInput)
        actions.perform()
        loginbuton=self.driver.find_element(By.ID,"login-button")
        loginbuton.click()
        errormessage=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errormessage.text == "Epic sadface: Sorry, this user has been locked out."    
    
        
