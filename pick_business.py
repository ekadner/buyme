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
        pick_category = self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//a[@role='button' and @title='גיפט קארד למותגי אופנה']")))
        self.execute_script("arguments[0].scrollIntoView();", pick_category)
        pick_category.click()

    def choose_gift_card(self):
        gift_card = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                     "//a[@aria-label='            \n\n        \n            \n        \n\n\n\n\n\n    \n        BUYME TOTAL FASHION\n    \n\n\n']")))
        gift_card.click()

    def fill_in_an_amount(self):
        amount = self.wait.until(
            expected_conditions.presence_of_element_located(By.XPATH, "//input[@placeholder='הכנס סכום']"))
        amount.send_keys("250")

    def click_submit_button(self):
        submit = self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.click()

    def assert_url(self):
        current_url = self.driver.current_url
        expected_url = "https://buyme.co.il"
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"
