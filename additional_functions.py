from selenium.webdriver.common.alert import Alert


class AdditionalFunctions:
    def __init__(self, driver):
        self.driver = driver

    def catch_pop_up(self):
        self.driver.execute_script("alert('This is an alert!');")
        alert = Alert(self.driver)
        alert.dismiss()
