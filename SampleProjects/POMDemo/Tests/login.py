from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from SampleProjects.POMDemo.Pages.loginPage import LoginPage
from SampleProjects.POMDemo.Pages.homePage import HomePage
import HtmlTestRunner
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    def test02_login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        self.assertEqual(message,"Invalid credentials")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))




