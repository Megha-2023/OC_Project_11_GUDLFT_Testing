from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
import unittest
from server import create_app


class FunctionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Flask test server
        cls.app = create_app()
        cls.app.testing = True
        cls.server_thread = threading.Thread(target=cls.app.run, kwargs={'port': 5000}, daemon=True)
        cls.server_thread.start()
        time.sleep(1)  # Give the server time to start

        # Set up Selenium WebDriver
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_login(self):
        
        self.driver.get("http://localhost:5000/")

        time.sleep(3)
        
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys("admin@irontemple.com")

        login_button = self.driver.find_element(By.ID, 'login')
        login_button.click()
        
        time.sleep(3)

        assert self.driver.current_url == "http://localhost:5000/showSummary"


if __name__ == "__main__":
    unittest.main()
