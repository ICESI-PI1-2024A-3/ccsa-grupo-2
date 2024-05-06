import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from requests_mgmt.models.request import Request
import time

class Assign_approver_exist(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
    
    def testAssign_approver(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        time.sleep(2)
        menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/button/span")
        menu.click()
        time.sleep(2)
        request=self.driver.find_element(By.XPATH, "//*[@id='offcanvasWithBothOptions']/div/div/a[3]")
        request.click()
        invoice_request=self.driver.find_element(By.XPATH,"/html/body/div[3]/table/tbody/tr[3]/td[1]")
        invoice_request.click()
        time.sleep(2)
        approver=self.driver.find_element(By.XPATH,"//*[@id='id_approvers']/option[3]")
        approver.click()
        time.sleep(2)
        assign=self.driver.find_element(By.XPATH,"/html/body/div/div[3]/div[5]/div/div[2]/form/button")
        assign.click()
        time.sleep(2)