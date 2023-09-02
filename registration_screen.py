from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationScreen:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_enter_button(self):
        click_enter_button = self.driver.find_element(By.CLASS_NAME, "notSigned")
        click_enter_button.click()

    def click_registration_button(self):
        click_registration_button = self.driver.find_element(By.XPATH, "//span[@class='text-link theme' and @aria-label='להרשמה' and @role='link' ]")
        click_registration_button.click()

    def fill_first_name_field(self):
        fill_first_name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='שם פרטי' and @tuaandiinputdiscrp='שם פרטי' and @type='text']")
        fill_first_name_field.send_keys("Jenny Kadner")

    def fill_email_field(self):
        fill_email_field = self.driver.find_element(By.XPATH, "//input[@placeholder='מייל' and @tuaandiinputdiscrp='* מייל' and @type='email']")
        fill_email_field.send_keys("Jenny@gmail.com")

    def fill_password_field(self):
        fill_password_field = self.driver.find_element(By.XPATH, "//input[@placeholder='סיסמה' and @tuaandiinputdiscrp='* סיסמה' and @type='password']")
        fill_password_field.send_keys("123456789")

    def fill_password_verification_field(self):
        fill_password_verification_field = self.driver.find_element(By.XPATH, "//input[@placeholder='אימות סיסמה' and @tuaandiinputdiscrp='אימות סיסמה' and @type='password']")
        fill_password_verification_field.send_keys("123456789")

    def press_submit_button(self):
        press_submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @gtm='הרשמה ל-BUYME' and @class='ember-view bm-btn no-reverse main md stretch']")
        press_submit_button.click()



# def main():
#     r_screen = RegistrationScreen()
#     r_screen.click_enter_button()

# class Shark:
#     def swim(self):
#         print("The shark is swimming")
#
#     def eat(self):
#         print("The shark is eating")
#
#
# def main():
#     sammy = Shark()
#     sammy.swim()
#     sammy.eat()
#
# main()