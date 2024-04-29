import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
##from . import constants as const

class Login(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        print("Inicia el Test")
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        text_expected = self.driver.find_element(By.XPATH, '/html/body/section/div[1]')
        self.assertEqual(text_expected.text, "Apoyo Logistico")

if __name__ == "_main_":
    unittest.main()