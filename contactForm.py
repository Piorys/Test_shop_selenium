# Target Site = http://automationpratice.com
# Scope of the test: Checking shopping cart by adding several items and increasing its quantity from the cart
#
# Steps:
#


import unittest
from selenium import webdriver

targetSite = "http://automationpractice.com"


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testForm(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get(targetSite)

        # Step
        contact_us = driver.find_element_by_xpath('//*[@id="contact-link"]/a')
        contact_us.click()

        # Step
        heading_dropdown = driver.find_element_by_id("id_contact")
        for option in heading_dropdown.find_elements_by_tag_name("option"):
            if option.text == "Customer service":
                option.click()
                break
        # Step
        form_mail = driver.find_element_by_id("email")
        form_mail.send_keys("dupajasiu@mail.com")

        # Step
        form_order_id = driver.find_element_by_id("id_order")
        form_order_id.send_keys("000000000")

        # Step
        form_message = driver.find_element_by_id("message")
        form_message.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis diam quam, semper at diam non, faucibus sollicitudin arcu. Duis hendrerit est id odio elementum, id ullamcorper nibh sollicitudin. Aliquam facilisis tempor metus, sit amet convallis purus tincidunt in. Nunc eu luctus tortor. Nulla nec tellus ultricies, bibendum urna ut, dapibus sapien. Etiam varius quam dictum, sollicitudin nibh ultrices, blandit sapien. Pellentesque elementum lectus id lectus vehicula, eu ornare magna placerat. Aliquam faucibus consectetur turpis, quis interdum metus luctus nec. Curabitur lacus justo, scelerisque vel neque a, egestas lacinia mi. Pellentesque in orci ipsum. Aenean at sollicitudin ipsum. Aliquam mollis purus nunc, et euismod lectus interdum ut.")

        # Step
        form_submit = driver.find_element_by_id("submitMessage")
        form_submit.click()

        # Step
        msg_div_text = driver.find_element_by_xpath('//*[@id="center_column"]').text

        self.assertTrue(msg_div_text, "Your message has been successfully sent to our team.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()






