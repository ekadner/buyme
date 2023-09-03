import time

import allure
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def login(self):
        login = self.driver.find_element(By.CLASS_NAME, "notSigned")
        login.click()
        time.sleep(1)
        fill_mail = self.driver.find_element(By.XPATH, "//input[@type='email']")
        fill_mail.send_keys('ekadner@gmail.com')
        fill_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
        fill_password.send_keys('4Ukiruki')
        remember_me_off = self.driver.find_element(By.CLASS_NAME, "fill")
        remember_me_off.click()
        submit = self.driver.find_element(By.TAG_NAME, "button")
        submit.click()

    def choose_an_amount(self):
        try:
            self.driver.find_element(By.XPATH, "//span[@class='selected-text' and @alt='סכום']").click()
            self.driver.find_element(By.XPATH, "//span[contains(text(), '200-299')]").click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_an_amount",
                              attachment_type=allure.attachment_type.PNG)
        except ElementClickInterceptedException:
            with allure.step("Element Click Intercepted"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_an_amount",
                              attachment_type=allure.attachment_type.PNG)

    def choose_an_area(self):
        try:
            self.driver.find_element(By.XPATH, "//span[@class='selected-text' and @alt='אזור']").click()
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'ירושלים')]").click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_an_area",
                              attachment_type=allure.attachment_type.PNG)
        except ElementClickInterceptedException:
            with allure.step("Element Click Intercepted"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_an_amount",
                              attachment_type=allure.attachment_type.PNG)

    def choose_a_category(self):
        try:
            self.driver.find_element(By.XPATH, "//span['קטגוריה'=.]").click()
            self.driver.find_element(By.XPATH, "//span[contains(text(), 'גיפט קארד למותגי אופנה')]").click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_a_category",
                              attachment_type=allure.attachment_type.PNG)
        except ElementClickInterceptedException:
            with allure.step("Element Click Intercepted"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_an_amount",
                              attachment_type=allure.attachment_type.PNG)

    def click_a_find_button(self):
        try:
            self.driver.find_element(By.XPATH, "//*[@id='ember1199']").click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="find_button",
                              attachment_type=allure.attachment_type.PNG)
