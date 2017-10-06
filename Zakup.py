# Target site =  automationpratice.com
# Scope of the test - Basic route of choosing item, customizing its color,size and buying it
#
# Test steps
# Step 1 - Choosing "T-Shirts" category
# Step 2 - Choosing "Faded short Sleeve T-Shirts" though "more" button
# Step 3 - Choosing Medium Size
# Step 4 - Choosing blue colour
# Step 5 - Adding item to basket
# Step 6 - "proceed to checkout"
# Step 7 - "proceed to checkout"
# Step 8 - Logging in with L: piotrryszewski@gmail.com P: dupajasiu
# Step 8 - "proceed to checkout"
# Step 9 - Checking "Terms of service"
# Step 10 - Choosing "Pay by bank wire"
# Step 11 - Confirming order

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://automationpractice.com"


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_buy_shirt(self):
        driver = self.driver
        driver.get(targetSite)

        # Step 1
        category_button = driver.find_element_by_partial_link_text("T-")
        category_button.click()

        # step 2
        more_button = driver.find_element_by_partial_link_text("Mor")
        more_button.click()

        # Step 3
        dropdown_size = driver.find_element_by_id("group_1")
        for option in dropdown_size.find_elements_by_tag_name("option"):
            if option.text == "M":
                option.click()
                break

        # Step 4
        color = driver.find_element_by_id("color_14")
        color.click()

        # Step 5
        add_to_cart = driver.find_element_by_id("add_to_cart")
        add_to_cart.click()

        # Step 6
        driver.implicitly_wait(20)
        proceed = driver.find_element_by_partial_link_text("Proceed")
        proceed.click()
        driver.implicitly_wait(20)

        # Step 7
        proceed_checkout = driver.find_element_by_partial_link_text("Proceed")
        proceed_checkout.click()

        # step 8

        login = driver.find_element_by_id("email")
        password = driver.find_element_by_id("passwd")
        sign_in = driver.find_element_by_id("SubmitLogin")

        login.send_keys("piotrryszewski@gmail.com")
        password.send_keys("dupajasiu")
        sign_in.click()

        # Step 9
        proceed_checkout = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button')
        proceed_checkout.click()

        # Step 10
        checkbox = driver.find_element_by_id("cgv")
        checkbox.click()

        # Step 11
        proceed_checkout = driver.find_element_by_xpath('//*[@id="form"]/p/button')
        proceed_checkout.click()

        # Step 12
        bankwire = driver.find_element_by_partial_link_text("bank wire")
        bankwire.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

