# Target Site = http://automationpratice.com
# Scope of the test: Checking shopping cart by adding several items and increasing its quantity from the cart
#
# Steps:
#


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

targetSite = "http://automationpractice.com"


class ShopTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testCart(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get(targetSite)

        # Step
        category_button = driver.find_element_by_partial_link_text("T-")
        category_button.click()

        # step
        more_button = driver.find_element_by_partial_link_text("Faded")
        more_button.click()

        # Step
        dropdown_size = driver.find_element_by_id("group_1")
        for option in dropdown_size.find_elements_by_tag_name("option"):
            if option.text == "M":
                option.click()
                break

        # Step
        color = driver.find_element_by_id("color_14")
        color.click()

        # Step
        add_to_cart = driver.find_element_by_id("add_to_cart")
        add_to_cart.click()

        # Step
        driver.implicitly_wait(20)
        proceed = driver.find_element_by_partial_link_text("Proceed")
        proceed.click()
        driver.implicitly_wait(20)

        # Step
        quantity_input = driver.find_element_by_xpath('//*[@id="product_1_4_0_0"]/td[5]/input[2]')
        quantity_input.clear()
        quantity_input.send_keys("999")

        # Step
        logo = driver.find_element_by_xpath('//*[@id="header_logo"]/a/img')
        logo.click()

        # Step
        quantity_check_num = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]').text
        self.assertTrue("999", quantity_check_num)

        # Step
        women_category = driver.find_element_by_partial_link_text("Women")
        women_category.click()

        # Step
        filter_tops = driver.find_element_by_id("layered_category_4")
        filter_tops.click()

        #Step
        filter_colour = driver.find_element_by_id("layered_id_attribute_group_11")
        filter_colour.click()

        #Step
        black_blouse_more = driver.find_element_by_partial_link_text("More")
        black_blouse_more.click()
        driver.implicitly_wait(20)

        #Step
        dropdown_size_black = driver.find_element_by_id("group_1")
        for option in dropdown_size_black.find_elements_by_tag_name("option"):
            if option.text == "L":
                option.click()
                break

        # Step
        add_to_cart = driver.find_element_by_id("add_to_cart")
        add_to_cart.click()

        # Step
        driver.implicitly_wait(20)
        proceed = driver.find_element_by_partial_link_text("Proceed")
        proceed.click()
        driver.implicitly_wait(20)

        # Step
        quantity_input_2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div[2]/table/tbody/tr[2]/td[5]/input[2]')
        quantity_input_2.clear()
        quantity_input_2.send_keys("1024")

        # Step
        proceed = driver.find_element_by_partial_link_text("Proceed")
        proceed.click()

        # Step
        login = driver.find_element_by_id("email")
        password = driver.find_element_by_id("passwd")
        sign_in = driver.find_element_by_id("SubmitLogin")

        login.send_keys("piotrryszewski@gmail.com")
        password.send_keys("dupajasiu")
        sign_in.click()

        # Step
        proceed_checkout = driver.find_element_by_xpath('//*[@id="center_column"]/form/p/button')
        proceed_checkout.click()

        # Step
        checkbox = driver.find_element_by_id("cgv")
        checkbox.click()

        # Step
        proceed_checkout = driver.find_element_by_xpath('//*[@id="form"]/p/button')
        proceed_checkout.click()

        # Step
        bankwire = driver.find_element_by_partial_link_text("bank wire")
        bankwire.click()

        # Step
        confirmation = driver.find_element_by_xpath('//*[@id="cart_navigation"]/button')
        confirmation.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

