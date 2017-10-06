# Pierwsze ćwiczenie z użyciem testowej strony automationpratice.com
# Cel - Przeprowadzenie podstawowej ścieżki zakupu
# Test case
# Krok 1 - Wybór kategorii T-shirts
# Krok 2 - Wybór produktu "Faded short Sleeve T-Shirts" za pomocą przycisku "more"
# Krok 3 - Wybór rozmiaru M
# Krok 4 - Wybór niebieskiego koloru
# Krok 5 - Dodanie wybranego produktu do koszyka
# Krok 6 - Naciśnięcie "proceed to checkout"
# Krok 7 - Naciśnięcie "proceed to checkout"
# Krok 8 - Zalogowanie się za pomocą danych L: piotrryszewski@gmail.com H: dupajasiu i wciśnięcie enter
# Krok 8 - Naciśnięcie "proceed to checkout"
# Krok 9 - Kliknięcie checkboxa Terms of service i naciśnięcie "proceed to checkout"
# Krok 10 - Wybór "Pay by bank wire"
# Krok 11 - Naciśnięcie "I confirm my order"

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://automationpractice.com"

class ShopTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # def test_check_title(self):
    #     driver = self.driver
    #     driver.get(targetSite)
    #     # Sprawdzenie czy w tytule znajduje się tekst "My Store"
    #     self.assertIn("My Store", driver.title)

    def test_buy_shirt(self):
        driver = self.driver
        driver.get(targetSite)

        # Wyszukanie i przejście do kategorii T-Shirts - Krok 1
        category_button = driver.find_element_by_partial_link_text("T-")
        category_button.click()

        # Wybór Produktu - Krok 2
        more_button = driver.find_element_by_partial_link_text("Mor")
        more_button.click()

        # Wybór rozmiaru - Krok 3
        dropdown_size = driver.find_element_by_id("group_1")
        for option in dropdown_size.find_elements_by_tag_name("option"):
            if option.text == "M":
                option.click()
                break

        # Wybór koloru - Krok 4
        color = driver.find_element_by_id("color_14")
        color.click()

        # Dodanie do koszyka - Krok 5
        add_to_cart = driver.find_element_by_id("add_to_cart")
        add_to_cart.click()

        # Proceed to checkout - Krok 6
        driver.implicitly_wait(20)
        proceed = driver.find_element_by_partial_link_text("Proceed")
        proceed.click()
        driver.implicitly_wait(20)

        # Proceed to checkout - Krok 7
        proceed_checkout = driver.find_element_by_partial_link_text("Proceed")
        proceed_checkout.click()



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

