import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

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
