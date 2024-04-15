import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By;


class StackAdaptAutomationTest(unittest.TestCase):

    def setUp(self):

        # look for register.html in the same directory as the Python script
        filePath = os.path.join(os.getcwd(), "register.html")
        
        self.driver = webdriver.Chrome()
        self.driver.get("file://" + filePath)        
        self.driver.maximize_window()

    def test_creation_and_distribution(self):
     
        # Fill in the register form with credentials
        email_input = self.driver.find_element(By.ID,'email')
        email_input.send_keys("username@domain.com")

        password_input = self.driver.find_element(By.ID,'psw')
        password_input.send_keys("MyStrongPassword123$")

        password_repeat = self.driver.find_element(By.ID, 'psw-repeat')
        password_repeat.send_keys("MyStrongPassword123$")
        # Click the Register button
        
        register_button = self.driver.find_element(By.CLASS_NAME, "registerbtn")
        time.sleep(5)
 
        self.driver.implicitly_wait(10)

        register_button.click()
 
        # Verify that the user is logged in by checking the presence of the profile button
        #profile_button = self.driver.find_element_by_xpath("//button[contains(@aria-label,'Profile')]")
        #self.assertTrue(profile_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()