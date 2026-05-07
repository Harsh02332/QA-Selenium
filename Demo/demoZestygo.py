import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ZestyRegistrationTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Safari WebDriver
        self.driver = webdriver.Safari()
        # Maximize the window so all form elements are visible on screen
        self.driver.maximize_window()
        self.addCleanup(self.driver.quit)

    def test_registration_form_submission(self):
        # 1. Navigate to the website's registration page
        self.driver.get('https://restaurants.zesty-go.com/')

        # 2. Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        
        # NOTE: If you need to click a "Sign Up" link to make the form appear,
        # you would do it here. Example (uncomment if needed):
        # signup_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
        # signup_link.click()

        print("\nLocating form fields...")
        
        # 3. Locate the input fields and type into them (.send_keys)
        # IMPORTANT: The locator names below (e.g., "first_name", "email") are placeholders. 
        # See my instructions below the code on how to find the exact names for your site!
        
        # Find the First Name field and type into it
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
        first_name_field.send_keys("TestUser")

        # Find the Last Name field
        last_name_field = self.driver.find_element(By.NAME, "last_name")
        last_name_field.send_keys("Automation")

        # Find the Email field
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("test_automation@example.com")

        # Find the Password field
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("SecurePassword123!")

        print("Submitting the form...")
        
        # 4. Locate and click the "Register" or "Submit" button
        # This XPATH looks for a button that either has type="submit" or says "Register"
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit' or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'register')]")
        submit_button.click()

        # 5. The Assertion (Did it work?)
        # After clicking submit, we wait to see if the URL changes (e.g., moving to a dashboard)
        try:
            wait.until(EC.url_changes(self.driver.current_url))
            print(f"Success! Form submitted. New URL is: {self.driver.current_url}")
            
            # We can assert that the word "dashboard" or "success" is in the new URL
            # self.assertIn("dashboard", self.driver.current_url.lower())
            
        except Exception:
            self.fail("The form was submitted, but the page did not redirect. Registration may have failed.")

if __name__ == '__main__':
    unittest.main(verbosity=2)