import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from requests_mgmt.models.request import Request
import time

class Assign_reviewer_exist(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
    
    def testAssign_reviewer(self):
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")
        loginButton = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/form/div[3]/div[1]/button")
        loginButton.click()
        time.sleep(5)
        menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/button/span")
        menu.click()
        time.sleep(5)
        request=self.driver.find_element(By.XPATH, "//*[@id='offcanvasWithBothOptions']/div/div/a[3]")
        request.click()
        time.sleep(5)
        chargeAccount = self.driver.find_element(By.XPATH,"/html/body/div[3]/table/tbody/tr[1]/td[1]/a")
        chargeAccount.click()
        time.sleep(5)
        reviewer=self.driver.find_element(By.NAME,"reviewers")
        reviewer.click()
        assign=self.driver.find_element(By.XPATH,"//*[@id='id_reviewers']/option[2]")
        assign.click()
        time.sleep(5)
        accept=self.driver.find_element(By.XPATH,"/html/body/div/div[3]/div[4]/div/div[1]/form/button")
        accept.click();
        close=self.driver.find_element(By.XPATH,"//*[@id='successModalReviewer']/div/div/div[3]/button")
        close.click()
