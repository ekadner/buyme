import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PickBusinessScreen:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 30)
        self.driver = driver

    def pick_category(self):
        try:
            pick_category = self.driver.find_element(By.XPATH,
                                                     "//a[@role='button' and @title='גיפט קארד למותגי אופנה']")
            pick_category.click()
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="pick_category",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def choose_gift_card(self):
        try:
            gift_card = self.driver.find_element(By.XPATH,
                                                 "//a[@aria-label='            \n\n        \n            \n        \n\n\n\n\n\n    \n        BUYME TOTAL FASHION\n    \n\n\n']")
            gift_card.click()
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="choose_gift_card",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def fill_in_an_amount(self):
        try:
            amount = self.driver.find_element(By.XPATH, "//input[@placeholder='הכנס סכום']")
            amount.send_keys("250")
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="fill_in_an_amount",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def click_submit_button(self):
        try:
            submit = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            submit.click()
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="submit_button",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def assert_url(self):
        current_url = self.driver.current_url
        expected_url = "https://buyme.co.il/money/20620?price=250"
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
