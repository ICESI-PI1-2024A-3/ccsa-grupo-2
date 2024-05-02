import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from requests_mgmt.models.request import Request
import time

class CreateChargeAccount(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_create_charge_account(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/button/span")
        menu.click()
        newRequestOption = self.driver.find_element(By.XPATH, "//*[@id='offcanvasWithBothOptions']/div/div/a[4]/div/span[2]")
        newRequestOption.click()
        chargeAccountOption = self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/a/div/div")
        chargeAccountOption.click()
        time.sleep(1)

        starting_request_number = len(Request.objects.all())
        
        user_name = self.driver.find_element(By.NAME, "user_name")
        user_name.send_keys("Arthur")
        time.sleep(1)

        user_id = self.driver.find_element(By.NAME, "user_id")
        user_id.send_keys("123")
        time.sleep(1)

        doc_type = self.driver.find_element(By.NAME, "document_type")
        doc_type.send_keys("Cédula de ciudadanía")
        time.sleep(1)

        amount = self.driver.find_element(By.NAME, "amount")
        amount.send_keys("100000")
        time.sleep(1)

        concept = self.driver.find_element(By.NAME, "concept")
        concept.send_keys("This is a concept")
        time.sleep(1)

        # Desplazar la página hacia abajo
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.execute_script("window.scrollTo(0,600);")

        # Esperar un momento para que la página se desplace completamente
        time.sleep(1)

        # Ahora el checkbox debería estar visible, puedes hacer clic en él
        check = self.driver.find_element(By.ID, "id_checkbox_choices_0")
        check.click()

        city = self.driver.find_element(By.NAME, "city")
        city.send_keys("Cali")
        time.sleep(1)

        date = self.driver.find_element(By.NAME, "date")
        date.send_keys("5/8/2024")
        time.sleep(1)

        #rent = self.driver.find_element(By.NAME, "rent_tax_declarant")
        #rent.click()

        bankName = self.driver.find_element(By.NAME, "bank_name")
        bankName.send_keys("TestBank")
        time.sleep(1)

        account_number = self.driver.find_element(By.NAME, "account_number")
        account_number.send_keys("189372")
        time.sleep(1)

        account_type = self.driver.find_element(By.NAME, "account_type")
        account_type.send_keys("Ahorro")
        time.sleep(1)

        cex_no = self.driver.find_element(By.NAME, "cex_no")
        cex_no.send_keys("236632")
        time.sleep(1)

        sendButton = self.driver.find_element(By.NAME, "submit_button")
        sendButton.click()
        time.sleep(1)

        final_request_number = len(Request.objects.all())

        print(starting_request_number)
        print(final_request_number)

        expected_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/h2')
        self.assertEqual(expected_element.text,'Solicitudes')

class CreateChargeAccount2(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_create_charge_account(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/button/span")
        menu.click()
        newRequestOption = self.driver.find_element(By.XPATH, "//*[@id='offcanvasWithBothOptions']/div/div/a[4]/div/span[2]")
        newRequestOption.click()
        chargeAccountOption = self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/a/div/div")
        chargeAccountOption.click()
        time.sleep(1)

        #starting_request_number = len(Request.objects.all())
        
        user_name = self.driver.find_element(By.NAME, "user_name")
        user_name.send_keys("Roberto")
        time.sleep(1)

        user_id = self.driver.find_element(By.NAME, "user_id")
        user_id.send_keys("999")
        time.sleep(1)

        doc_type = self.driver.find_element(By.NAME, "document_type")
        doc_type.send_keys("Cédula de ciudadanía")
        time.sleep(1)

        amount = self.driver.find_element(By.NAME, "amount")
        amount.send_keys("40000")
        time.sleep(1)

        concept = self.driver.find_element(By.NAME, "concept")
        concept.send_keys("This is a concept")
        time.sleep(1)

        # Desplazar la página hacia abajo
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.execute_script("window.scrollTo(0,600);")

        # Esperar un momento para que la página se desplace completamente

        # Ahora el checkbox debería estar visible, puedes hacer clic en él
        check = self.driver.find_element(By.ID, "id_checkbox_choices_0")
        check.click()

        city = self.driver.find_element(By.NAME, "city")
        city.send_keys("Medellin")

        date = self.driver.find_element(By.NAME, "date")
        date.send_keys("2/3/2024")
        time.sleep(1)

        #rent = self.driver.find_element(By.NAME, "rent_tax_declarant")
        #rent.click()

        bankName = self.driver.find_element(By.NAME, "bank_name")
        bankName.send_keys("Bank")
        time.sleep(1)

        account_number = self.driver.find_element(By.NAME, "account_number")
        account_number.send_keys("635270")
        time.sleep(1)

        account_type = self.driver.find_element(By.NAME, "account_type")
        account_type.send_keys("Ahorro")
        time.sleep(1)

        cex_no = self.driver.find_element(By.NAME, "cex_no")
        cex_no.send_keys("42725")
        time.sleep(1)

        sendButton = self.driver.find_element(By.NAME, "submit_button")
        sendButton.click()
        time.sleep(1)

        #final_request_number = len(Request.objects.all())

        #print(starting_request_number)
        #print(final_request_number)

        expected_element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/h2')
        self.assertEqual(expected_element.text,'Solicitudes')

if __name__ == "_main_":
    unittest.main()