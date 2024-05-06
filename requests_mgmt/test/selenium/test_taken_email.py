import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import random

class TakenEmail(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_taken_email(self):
        registerButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[2]/a")
        registerButton.click()
        firstName = self.driver.find_element(By.NAME, "first_name")
        firstName.send_keys("Morgan")

        lastName = self.driver.find_element(By.NAME, "last_name")
        lastName.send_keys("Le Fay")
        phone = self.driver.find_element(By.NAME, "phone")
        phone.send_keys("3144972043")

        id_type = self.driver.find_element(By.NAME, "id_type")
        id_type.send_keys("Cédula de Ciudadanía")

        number = random.randint(1000,10000)
        id_number = self.driver.find_element(By.NAME, "id_number")
        id_number.send_keys(f"{number}")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("user@mail.com")

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("password123")

        password_confirm = self.driver.find_element(By.NAME, "password_confirm")
        password_confirm.send_keys("password123")

        sendButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[9]/div[1]/button")
        sendButton.click()

        text_expected = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div')
        self.assertEqual(text_expected.text, "El email ya está registrado")
    
    


if __name__ == "_main_":
    unittest.main()