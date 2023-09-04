import json
import time
from unittest import TestCase
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from registration_screen import RegistrationScreen
from pick_business import PickBusinessScreen
from home_screen import HomeScreen
from sender_receiver_information_screen import SenderReceiverInformationScreen
from additional_functions import AdditionalFunctions


class TestBuyMe(TestCase):

    def setUp(self):
        json_file = open('data.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        if browser == 'chrome':
            self.driver = webdriver.Chrome(service=Service('C:\\Program Files\\chromedriver-win64\\chromedriver.exe'))
        url = data['URL']
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.RegistrationScreen = RegistrationScreen(self.driver)
        self.PickBusinessScreen = PickBusinessScreen(self.driver)
        self.home_screen = HomeScreen(self.driver)
        self.sender_receiver_information_screen = SenderReceiverInformationScreen(self.driver)
        self.additional_functions = AdditionalFunctions(self.driver)
        print('start testing BUY ME')

    def test_registration_screen(self):
        RegistrationScreen.click_enter_button(self)
        RegistrationScreen.click_registration_button(self)
        RegistrationScreen.fill_first_name_field(self)
        RegistrationScreen.fill_email_field(self)
        RegistrationScreen.fill_password_field(self)
        RegistrationScreen.fill_password_verification_field(self)
        RegistrationScreen.press_submit_button(self)

    def test_pick_business_screen(self):
        AdditionalFunctions.catch_pop_up(self)
        PickBusinessScreen.pick_category(self)
        PickBusinessScreen.choose_gift_card(self)
        PickBusinessScreen.fill_in_an_amount(self)
        PickBusinessScreen.click_submit_button(self)
        PickBusinessScreen.assert_url(self)

    def test_home_screen(self):
        AdditionalFunctions.catch_pop_up(self)
        # HomeScreen.login(self) פונקצייה סגורה בגלל חלון אימות
        HomeScreen.choose_an_amount(self)
        HomeScreen.choose_an_area(self)
        HomeScreen.choose_a_category(self)
        HomeScreen.click_a_find_button(self)

    def test_sender_receiver_information_screen(self):
        AdditionalFunctions.catch_pop_up(self)
        SenderReceiverInformationScreen.go_to_page(self)
        SenderReceiverInformationScreen.change_to_for_me(self)
        SenderReceiverInformationScreen.change_to_for_someone(self)
        SenderReceiverInformationScreen.input_name(self)
        SenderReceiverInformationScreen.define_event(self)
        SenderReceiverInformationScreen.write_a_greeting(self)
        SenderReceiverInformationScreen.upload_a_picture(self)
        SenderReceiverInformationScreen.click_submit_button(self)
        SenderReceiverInformationScreen.change_to_send_later(self)
        SenderReceiverInformationScreen.change_to_send_now(self)
        SenderReceiverInformationScreen.select_sms_as_way_to_send(self)
        SenderReceiverInformationScreen.enter_the_recipients_phone_number(self)
        SenderReceiverInformationScreen.enter_senders_name(self)
        SenderReceiverInformationScreen.enter_senders_phone_number(self)
        SenderReceiverInformationScreen.proceed_to_payment_button(self)

    def tearDown(self):
        self.driver.quit()
