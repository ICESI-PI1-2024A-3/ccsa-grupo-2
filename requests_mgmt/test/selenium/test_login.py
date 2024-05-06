import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import random

class Login(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys("123")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")

        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()

        text_expected = self.driver.find_element(By.NAME, 'welcome')
        self.assertEqual(text_expected.text, "Bienvenido")

class LoginUnextistingUser(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_failed(self):
        user_name = self.driver.find_element(By.NAME, "username")
        number = random.randint(1000,10000)
        user_name.send_keys(f"{number}")
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("password")
        time.sleep(1)
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        time.sleep(1)

        text_expected = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div')
        self.assertEqual(text_expected.text, "Usuario o contraseña incorrectos")

class LoginWrongPassword(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_Wrong_password(self):
        user_name = self.driver.find_element(By.NAME, "username")
        
        user_name.send_keys(f"123")
        time.sleep(1)
        password = self.driver.find_element(By.NAME, "password")
        number = random.randint(1000,10000)
        password.send_keys(f"IncorrectPassword{number}")
        time.sleep(1)
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        time.sleep(1)

        text_expected = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div')
        self.assertEqual(text_expected.text, "Usuario o contraseña incorrectos")


if __name__ == "_main_":
    unittest.main()