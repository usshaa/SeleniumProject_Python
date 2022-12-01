from selenium.webdriver.common.by import By
from SampleProjects.POMDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidUsername_message_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_invalid_username_message(self,message):
        msg=self.driver.find_element(By.XPATH,self.invalidUsername_message_xpath).text
        return msg