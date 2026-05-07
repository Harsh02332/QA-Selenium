import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get('https://monolithicsc.com')


if __name__ == '__main__':
    unittest.main(verbosity=2)