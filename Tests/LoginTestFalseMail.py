import unittest
from selenium import webdriver

targetSite = "http://automationpractice.com"


class LoginTestFalseMail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testForm(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get(targetSite)
    # Step
        sign_in_link = driver.find_element_by_class_name("login")
        sign_in_link.click()

    # Step
        mail_prompt = driver.find_element_by_id("email")
        mail_prompt.send_keys("dupajasiu123@gmail.com")

    # Step
        password_prompt = driver.find_element_by_id("passwd")
        password_prompt.send_keys("dupajasiu")

    # Step
        submit_login = driver.find_element_by_id("SubmitLogin")
        submit_login.click()
    # Step
        err_msg = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li').text
        self.assertIn("Authentication failed.", err_msg)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()