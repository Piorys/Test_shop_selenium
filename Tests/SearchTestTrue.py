import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://automationpractice.com"


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearchDress(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get(targetSite)
    # Step
        search_box = driver.find_element_by_id("search_query_top")
        search_box.clear()
        search_box.send_keys("dress")
        search_box.send_keys(Keys.ENTER)

    # Step
        results_counter = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[2]').text
        self.assertTrue("have been found", results_counter)


def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
        unittest.main()
