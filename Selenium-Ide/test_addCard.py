# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddCard():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addCard(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
  
