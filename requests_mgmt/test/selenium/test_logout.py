import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class Logout(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_logout(self):
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys("123")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        time.sleep(1)
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        time.sleep(1)
        exit_btn = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/div/a")
        exit_btn.click()
        time.sleep(1)

        text_expected = self.driver.find_element(By.NAME, 'submit_btn')

        self.assertEqual(text_expected.text, "Iniciar Sesión")

if __name__ == "_main_":
    unittest.main()