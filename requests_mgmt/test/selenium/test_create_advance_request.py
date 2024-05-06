import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from requests_mgmt.models.request import Request
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

class TestCreateAdvanceRequest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_create_advance_request_1(self):
        self.fill_form("John Doe", "12345", "Passport", "10/04/2024", "05/05/2024", "Engineering Department", "Business trip", "New York", "20/04/2024", "25/04/2024", "US Dollars", "1000000", "75000", "200000", "400000", "70000", "100000")

    def test_create_advance_request_2(self):
        self.fill_form("Jane Smith", "67890", "ID Card", "12/04/2024", "07/05/2024", "Marketing Department", "Conference", "London", "22/04/2024", "27/04/2024", "Euros", "1200000", "80000", "250000", "450000", "80000", "120000")

    def test_create_advance_request_3(self):
        self.fill_form("Michael Johnson", "54321", "Driver's License", "15/04/2024", "10/05/2024", "HR Department", "Interview", "Paris", "25/04/2024", "30/04/2024", "Pounds Sterling", "900000", "70000", "180000", "350000", "60000", "90000")

    def test_create_advance_request_4(self):
        self.fill_form("Luisa Fernanda Gómez", "765432", "Cédula de Ciudadanía", "10/05/2024", "15/06/2024", "Departamento de Finanzas", "Capacitación", "Madrid", "20/05/2024", "25/05/2024", "Euros", "1500000", "90000", "300000", "500000", "100000", "200000")

    def test_create_advance_request_5(self):
        self.fill_form("Carlos Andrés López", "234567", "Tarjeta de Identidad", "12/05/2024", "17/06/2024", "Departamento de Ventas", "Reunión de Negocios", "Buenos Aires", "22/05/2024", "27/05/2024", "Pesos Argentinos", "1300000", "85000", "280000", "450000", "85000", "130000")

    def test_create_advance_request_6(self):
        self.fill_form("María Fernanda Ramírez", "876543", "Cédula de Ciudadanía", "15/05/2024", "20/06/2024", "Departamento de Recursos Humanos", "Entrevista", "Santiago de Chile", "25/05/2024", "30/05/2024", "Pesos Chilenos", "1100000", "80000", "250000", "400000", "75000", "110000")

    def test_create_advance_request_7(self):
        self.fill_form("Juan Pablo Herrera", "345678", "Cédula de Ciudadanía", "18/05/2024", "23/06/2024", "Departamento de Logística", "Visita a Proveedores", "Ciudad de México", "28/05/2024", "02/06/2024", "Pesos Mexicanos", "1250000", "85000", "270000", "430000", "90000", "125000")

    def test_create_advance_request_8(self):
        self.fill_form("Laura Rodríguez", "987654", "Cédula de Ciudadanía", "20/05/2024", "25/06/2024", "Departamento de Tecnología", "Congreso", "Río de Janeiro", "30/05/2024", "04/06/2024", "Reales Brasileños", "1400000", "95000", "320000", "480000", "95000", "140000")

    def test_create_advance_request_9(self):
        self.fill_form("Camilo Sánchez", "456789", "Cédula de Ciudadanía", "22/05/2024", "27/06/2024", "Departamento de Investigación y Desarrollo", "Presentación de Producto", "Tokio", "01/06/2024", "06/06/2024", "Yenes Japoneses", "1600000", "100000", "350000", "520000", "100000", "160000")

    def test_create_advance_request_10(self):
        self.fill_form("Valentina Gutiérrez", "876543", "Cédula de Ciudadanía", "25/05/2024", "30/06/2024", "Departamento de Contabilidad", "Auditoría Externa", "Berlín", "05/06/2024", "10/06/2024", "Euros", "1700000", "105000", "380000", "550000", "105000", "170000")

    def test_create_advance_request_11(self):
        self.fill_form("Andrés Felipe Martínez", "654321", "Cédula de Ciudadanía", "28/05/2024", "03/07/2024", "Departamento de Marketing", "Lanzamiento de Producto", "Roma", "08/06/2024", "13/06/2024", "Euros", "1800000", "110000", "400000", "600000", "110000", "180000")

    def test_create_advance_request_12(self):
        self.fill_form("Diana López", "234567", "Cédula de Ciudadanía", "30/05/2024", "05/07/2024", "Departamento de Producción", "Capacitación", "Ciudad del Cabo", "10/06/2024", "15/06/2024", "Rand Sudafricano", "1900000", "115000", "420000", "650000", "115000", "190000")

    def test_create_advance_request_13(self):
        self.fill_form("Santiago Gómez", "345678", "Cédula de Ciudadanía", "01/06/2024", "07/07/2024", "Departamento de Ventas", "Negociación de Contrato", "Sídney", "12/06/2024", "17/06/2024", "Dólares Australianos", "2000000", "120000", "450000", "700000", "120000", "200000")

    def test_create_advance_request_14(self):
        self.fill_form("Laura Pérez", "456789", "Cédula de Ciudadanía", "03/06/2024", "09/07/2024", "Departamento de Recursos Humanos", "Reclutamiento", "Nueva Delhi", "14/06/2024", "19/06/2024", "Rupia India", "2100000", "125000", "480000", "750000", "125000", "210000")

    def test_create_advance_request_15(self):
        self.fill_form("Mateo Rodríguez", "567890", "Cédula de Ciudadanía", "05/06/2024", "11/07/2024", "Departamento de Logística", "Suministro de Materiales", "Singapur", "16/06/2024", "21/06/2024", "Dólares de Singapur", "2200000", "130000", "510000", "800000", "130000", "220000")


    def fill_form(self, user_name, user_id, doc_type, request_date, return_date, user_dependency, reason_trip, destination_city, departure_date, icesi_last_day_date, advance_currency, airport_transport, local_transport, feeding, accommodation, departure_taxes, others):
        # Fill the form with provided data
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys("123")  
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("123")  
        loginButton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        loginButton.click()

        menu = self.driver.find_element(By.XPATH, "/html/body/div[1]/button")
        menu.click()
        #time.sleep(1)
        newRequestOption = self.driver.find_element(By.XPATH, "//*[@id='offcanvasWithBothOptions']/div/div/a[2]/div")
        newRequestOption.click()
        #time.sleep(1)

        advanceRequesttOption = self.driver.find_element(By.XPATH, "/html/body/main/div/div[3]")
        advanceRequesttOption.click()
        #time.sleep(1)

        user_name_field = self.driver.find_element(By.NAME, "user_name")
        user_name_field.send_keys(user_name)
        #time.sleep(1)

        user_id_field = self.driver.find_element(By.NAME, "user_id")
        user_id_field.send_keys(user_id)
        #time.sleep(1)

        doc_type_field = self.driver.find_element(By.NAME, "document_type")
        doc_type_field.send_keys(doc_type)
        #time.sleep(1)

        request_date_field = self.driver.find_element(By.NAME, "request_date")
        request_date_field.send_keys(request_date)
        #time.sleep(1)

        return_date_field = self.driver.find_element(By.NAME, "return_date")
        return_date_field.send_keys(return_date)
        #time.sleep(1)

        user_dependency_field = self.driver.find_element(By.NAME, "dependency")
        user_dependency_field.send_keys(user_dependency)
        #time.sleep(1)

        reason_trip_field = self.driver.find_element(By.NAME, "reason_trip")
        reason_trip_field.send_keys(reason_trip)
        #time.sleep(1)

        destination_city_field = self.driver.find_element(By.NAME, "destination_city")
        destination_city_field.send_keys(destination_city)
        #time.sleep(1)

        departure_date_field = self.driver.find_element(By.NAME, "departure_date")
        departure_date_field.send_keys(departure_date)
        #time.sleep(1)

        icesi_last_day_date_field = self.driver.find_element(By.NAME, "icesi_last_day_date")
        icesi_last_day_date_field.send_keys(icesi_last_day_date)
        #time.sleep(1)

        advance_currency_field = self.driver.find_element(By.NAME, "advance_currency")
        advance_currency_field.send_keys(advance_currency)
        #time.sleep(1)

        airport_transport_field = self.driver.find_element(By.NAME, "airport_transport")
        airport_transport_field.send_keys(airport_transport)
        #time.sleep(1)

        local_transport_field = self.driver.find_element(By.NAME, "local_transport")
        local_transport_field.send_keys(local_transport)
        #time.sleep(1)

        feeding_field = self.driver.find_element(By.NAME, "feeding")
        feeding_field.send_keys(feeding)
        #time.sleep(1)

        accommodation_field = self.driver.find_element(By.NAME, "accommodation")
        accommodation_field.send_keys(accommodation)
        #time.sleep(1)

        departure_taxes_field = self.driver.find_element(By.NAME, "departure_taxes")
        departure_taxes_field.send_keys(departure_taxes)
        #time.sleep(1)

        others_field = self.driver.find_element(By.NAME, "others")
        others_field.send_keys(others)
        #time.sleep(1)

        sendButton = self.driver.find_element(By.NAME, "submit_button")
        self.driver.execute_script("arguments[0].click();", sendButton)
        #time.sleep(1)

        expected_element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/h2")
        self.assertEqual(expected_element.text, 'Solicitudes')
        #time.sleep(1)

if __name__ == "__main__":
    unittest.main()
