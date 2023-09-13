import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class SenderReceiverInformationScreen:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get('https://buyme.co.il/money/20620?price=250')

    def change_to_for_me(self):
        try:
            for_me = self.driver.find_element(By.XPATH, "//div[@gtm='לעצמי' and @role='Radio']")
            for_me.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="for_me",
                              attachment_type=allure.attachment_type.PNG)

    def change_to_for_someone(self):
        try:
            for_someone = self.driver.find_element(By.XPATH, "//div[@gtm='למישהו אחר' and @ role='Radio']")
            for_someone.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="for_someone",
                              attachment_type=allure.attachment_type.PNG)

    def input_name(self):
        try:
            name = self.driver.find_elements(By.XPATH, "//input[@class='ember-view ember-text-field']")
            name[0].send_keys("Jenny")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="input_name",
                              attachment_type=allure.attachment_type.PNG)

    def define_event(self):
        try:
            self.driver.find_element(By.XPATH, "//span['לאיזה אירוע?'=.]").click()
            self.driver.find_element(By.XPATH, "//span['יום הולדת'=.]").click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="define_event",
                              attachment_type=allure.attachment_type.PNG)

    def write_a_greeting(self):
        try:
            clear_a_field = self.driver.find_element(By.XPATH, "//span['נקה הכל'=.]")
            clear_a_field.click()
            greeting = self.driver.find_element(By.XPATH,
                                                "//textarea[@rows='4' and @data-parsley-group='voucher-greeting']")
            greeting.send_keys(
             "They say the older you are, the smarter you become. At your age you must be a genius! Happy birthday!")
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="write_a_greeting",
                              attachment_type=allure.attachment_type.PNG)

    def upload_a_picture(self):
        try:
            picture = self.driver.find_element(By.XPATH,
                                               "//input[@class='ember-view ember-text-field' and @accept='image/png,image/jpeg,video/quicktime,video/mp4,.mov,.qt']")
            picture.send_keys('C:\\Users\\ekadn\\Pictures\\donkey.jpg')
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="upload_a_picture",
                              attachment_type=allure.attachment_type.PNG)

    def click_submit_button(self):
        try:
            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and @gtm='המשך']")
            submit_button.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="submit_button",
                              attachment_type=allure.attachment_type.PNG)

    def change_to_send_later(self):
        try:
            send_later = self.driver.find_element(By.XPATH, "//div[@gtm='במועד מאוחר יותר' and @role='Radio']")
            send_later.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="send_later",
                              attachment_type=allure.attachment_type.PNG)

    def change_to_send_now(self):
        try:
            send_now = self.driver.find_element(By.XPATH, "//div[@gtm='עכשיו' and @role='Radio']")
            send_now.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="send_now",
                              attachment_type=allure.attachment_type.PNG)

    def select_sms_as_way_to_send(self):
        try:
            select_sms = self.driver.find_elements(By.XPATH, "//div[@class='circle-area']")
            select_sms[0].click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="sms_as_way_to_send",
                              attachment_type=allure.attachment_type.PNG)

    def enter_the_recipients_phone_number(self):
        try:
            recipients_phone_number = self.driver.find_element(By.XPATH, "//input[@id='sms']")
            recipients_phone_number.send_keys('0504080473')
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="recipients_phone_number",
                              attachment_type=allure.attachment_type.PNG)

    def enter_senders_name(self):
        try:
            senders_name = self.driver.find_element(By.XPATH, "//input[@placeholder='שם שולח המתנה']")
            senders_name.send_keys('Jenny')
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="senders_name",
                              attachment_type=allure.attachment_type.PNG)

    def enter_senders_phone_number(self):
        try:
            senders_phone_number = self.driver.find_element(By.XPATH, "//input[@placeholder='מספר נייד']")
            senders_phone_number.send_keys('0507863343')
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="senders_phone_number",
                              attachment_type=allure.attachment_type.PNG)

    def proceed_to_payment_button(self):
        try:
            proceed_to_payment = self.driver.find_element(By.XPATH, "//button[@type='submit' and @gtm='המשך לתשלום']")
            proceed_to_payment.click()
        except NoSuchElementException:
            with allure.step("Element not found"):
                allure.attach(self.driver.get_screenshot_as_png(), name="payment_button",
                              attachment_type=allure.attachment_type.PNG)

