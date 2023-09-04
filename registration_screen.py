import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



class RegistrationScreen:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_enter_button(self):
        try:
            click_enter_button = self.driver.find_element(By.CLASS_NAME, "notSigned")
            click_enter_button.click()
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="enter_button",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def click_registration_button(self):
        try:
            click_registration_button = self.driver.find_element(By.XPATH,
                                                                 "//span[@class='text-link theme' and @aria-label='להרשמה' and @role='link' ]")
            click_registration_button.click()
        except NoSuchElementException as e:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="registration_button",
                              attachment_type=allure.attachment_type.PNG)
                allure.attach(str(e), name="exception", attachment_type=allure.attachment_type.TEXT)

    def fill_first_name_field(self):
        try:
            fill_first_name_field = self.driver.find_element(By.XPATH,
                                                             "//input[@placeholder='שם פרטי' and @tuaandiinputdiscrp='שם פרטי' and @type='text']")
            fill_first_name_field.send_keys("Jenny Kadner")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="first_name_field",
                              attachment_type=allure.attachment_type.PNG)

    def fill_email_field(self):
        try:
            fill_email_field = self.driver.find_element(By.XPATH,
                                                        "//input[@placeholder='מייל' and @tuaandiinputdiscrp='* מייל' and @type='email']")
            fill_email_field.send_keys("Jenny@gmail.com")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="email_field",
                              attachment_type=allure.attachment_type.PNG)

    def fill_password_field(self):
        try:
            fill_password_field = self.driver.find_element(By.XPATH,
                                                           "//input[@placeholder='סיסמה' and @tuaandiinputdiscrp='* סיסמה' and @type='password']")
            fill_password_field.send_keys("123456789")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="password_field",
                              attachment_type=allure.attachment_type.PNG)

    def fill_password_verification_field(self):
        try:
            fill_password_verification_field = self.driver.find_element(By.XPATH,
                                                                        "//input[@placeholder='אימות סיסמה' and @tuaandiinputdiscrp='אימות סיסמה' and @type='password']")
            fill_password_verification_field.send_keys("123456789")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="password_verification_field",
                              attachment_type=allure.attachment_type.PNG)

    def press_submit_button(self):
        try:
            press_submit_button = self.driver.find_element(By.XPATH,
                                                           "//button[@type='submit' and @gtm='הרשמה ל-BUYME' and @class='ember-view bm-btn no-reverse main md stretch']")
            press_submit_button.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="submit_button",
                              attachment_type=allure.attachment_type.PNG)


# def click_enter_button(self):
#      click_enter_button = self.wait.until(
#          expected_conditions.element_to_be_clickable(By.CLASS_NAME, "notSigned"))
#      click_enter_button.click()
#
#  def click_registration_button(self):
#      click_registration_button = self.wait.until(expected_conditions.element_to_be_clickabl
#              (By.XPATH, "//span[@class='text-link theme' and @aria-label='להרשמה' and @role='link' ]"))
#      click_registration_button.click()
#
#  def fill_first_name_field(self):
#      self.WebDriverWait(self.driver, 10).until(
#          expected_conditions.presence_of_element_located(
#              (By.XPATH, "//input[@placeholder='שם פרטי' and @tuaandiinputdiscrp='שם פרטי' and @type='text']"))).send_keys("Jenny")
#
