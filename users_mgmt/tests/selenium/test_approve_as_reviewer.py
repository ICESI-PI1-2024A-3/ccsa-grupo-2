from telnetlib import EC
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

from selenium.webdriver.common.keys import Keys

class TestApprovalProcess(StaticLiveServerTestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitlywait(15)
        self.driver.maximizewindow()

    def tearDown(self):
        self.driver.quit()

    def test_approval_page(self):
        # Navegar a la página de solicitudes por revisar
        self.driver.get("http://127.0.0.1:8000/approve_as_reviewer/")  

        # Esperar a que la página se cargue completamente
        WebDriverWait(self.driver, 10).until( # type: ignore
            EC.presence_of_element_located((By.CLASS_NAME, "custom-card"))
        )

        # Verificar que existan elementos en la página
        requests_elements = self.driver.find_elements_by_class_name("custom-card")
        self.assertTrue(len(requests_elements) > 0)  # Verificar que haya al menos una solicitud por revisar

if __name__ == "__main__":
    unittest.main()
        
class ApproveAsReviewer(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_approve_as_reviewer(self):
        acceptButton = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/form/div[2]/button[1]")
        acceptButton.click()
        time.sleep(1)

        text_expected = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/h2')
        self.assertEqual(text_expected.text, "Solicitudes por revisar")
        
class RejectAsReviewer(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        
    def test_reject_as_reviewer(self):
        rejectButton = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/form/div[2]/button[2]")
        rejectButton.click()
        time.sleep(1)

        text_expected = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/h2')
        self.assertEqual(text_expected.text, "Solicitudes por revisar")

if __name__ == "__main__":
    unittest.main()
