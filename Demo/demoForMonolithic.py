import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MonolithicTestCase(unittest.TestCase):

    def setUp(self):
        # Using Safari to match your current setup
        self.driver = webdriver.Safari()
        self.addCleanup(self.driver.quit)

    def test_homepage_loads_successfully(self):
        # 1. Navigate to the specific website
        self.driver.get('https://monolithicsc.com/')

        # 2. Wait for the page to load (Best Practice)
        # This tells Selenium to wait up to 10 seconds for the 'body' of the website to appear.
        # If it doesn't appear within 10 seconds, the test will fail.
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 3. Run an Assertion (The actual test)
        # We grab the page title and assert that it actually contains text.
        page_title = self.driver.title
        
        # This will throw an error if the page title is completely empty.
        self.assertTrue(len(page_title) > 0, "The page title is empty, the site may not have loaded correctly.")

        # Print the title to your terminal so you can verify what Selenium saw
        print(f"\nSuccess! The website loaded and the title is: '{page_title}'")

if __name__ == '__main__':
    # Changed verbosity to 2 so it prints a slightly cleaner output
    unittest.main(verbosity=2)