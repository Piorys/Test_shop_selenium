import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://automationpractice.com"


class SearchTestFalse(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearchDressFalse(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get(targetSite)
    # Step
        search_box = driver.find_element_by_id("search_query_top")
        search_box.clear()
        search_box.send_keys("januszbujasienakrzesle")
        search_box.send_keys(Keys.ENTER)

    # Step
        no_results_alert = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        self.assertTrue("No results were found", no_results_alert)


def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
        unittest.main()
