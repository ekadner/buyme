from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class AdditionalFunctions:
    def __init__(self, driver):
        self.driver = driver

    def Catch_Pop_Up(self):
        self.driver.execute_script("alert('This is an alert!');")
        alert = Alert(self.driver)
        alert.dismiss()



