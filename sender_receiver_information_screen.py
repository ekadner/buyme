from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SenderReceiverInformationScreen:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 30)
        self.driver = driver

    def go_to_page(self):
        self.driver.get('https://buyme.co.il/money/20620?price=250')

    def change_to_for_me(self):
        for_me = self.driver.find_element(By.XPATH, "//div[@gtm='לעצמי' and @role='Radio']")
        for_me.click()

    def change_to_for_someone(self):
        for_someone = self.driver.find_element(By.XPATH, "//div[@gtm='למישהו אחר' and @ role='Radio']")
        for_someone.click()

    def input_name(self):  # שם המקבל מתנה
        name = self.driver.find_element(By.XPATH, "//input[@title='שם מקבל המתנה']")
        name.send_keys("Jenny")

    def define_event(self):  # בחירת אירוע
        self.driver.find_element(By.XPATH, "//span['לאיזה אירוע?'=.]").click()
        self.driver.find_element(By.XPATH, "//span['יום הולדת'=.]").click()

    def write_a_greeting(self):
        clear_a_field = self.driver.find_element(By.XPATH,
                                                 "//span[@class='textarea-clear-all ' and @aria-label='נקה הכל']")
        clear_a_field.click()
        greeting = self.driver.find_element(By.XPATH,
                                            "//textarea[@rows='4' and @data-parsley-group='voucher-greeting']")
        greeting.send_keys(
            "They say the older you are, the smarter you become. At your age you must be a genius! Happy birthday!")

    def upload_a_picture(self):
        picture = self.driver.find_element(By.XPATH,
                                           "//input[@class='ember-view ember-text-field' and @accept='image/png,image/jpeg,video/quicktime,video/mp4,.mov,.qt']")
        picture.send_keys('C:\\Users\\ekadn\\Pictures\\donkey.jpg')

    def click_submit_button(self):
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @gtm='המשך']")
        submit_button.click()

    def change_to_send_later(self):
        send_later = self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@gtm='במועד מאוחר יותר' and @role='Radio']")))
        send_later.click()

    def change_to_send_now(self):
        send_now = self.wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@gtm='עכשיו' and @role='Radio']")))
        send_now.click()

    def select_sms_as_way_to_send(self):
        select_sms = self.driver.find_elements(By.XPATH, "//div[@class='circle-area']")
        select_sms[0].click()

    def enter_the_recipients_phone_number(self):
        recipients_phone_number = self.driver.find_element(By.XPATH, "//input[@id='sms']")
        recipients_phone_number.send_keys('0504080473')

    def enter_senders_name(self):
        senders_name = self.driver.find_element(By.XPATH, "//input[@placeholder='שם שולח המתנה']")
        senders_name.send_keys('Jenny')

    def enter_senders_phone_number(self):
        senders_phone_number = self.driver.find_element(By.XPATH, "//input[@placeholder='מספר נייד']")
        senders_phone_number.send_keys('0507863343')

    def proceed_to_payment_button(self):
        proceed_to_payment = self.driver.find_element(By.XPATH, "//button[@type='submit' and @gtm='המשך לתשלום']")
        proceed_to_payment.click()
