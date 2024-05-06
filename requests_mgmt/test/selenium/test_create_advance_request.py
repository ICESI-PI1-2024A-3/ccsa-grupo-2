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
        self.fill_form("John Doe", "12345", "Cédula de extranjería", "10/04/2024", "05/05/2024", "Engineering Department", "Business trip", "New York", "20/04/2024", "25/04/2024", "US Dollars", "1000000", "75000", "200000", "400000", "70000", "100000")

    def test_create_advance_request_2(self):
        self.fill_form("Jane Smith", "67890", "Cédula de extranjería", "12/04/2024", "07/05/2024", "Marketing Department", "Conference", "London", "22/04/2024", "27/04/2024", "Euros", "1200000", "80000", "250000", "450000", "80000", "120000")

    def test_create_advance_request_3(self):
        self.fill_form("Michael Johnson", "54321", "Cédula de extranjería", "15/04/2024", "10/05/2024", "HR Department", "Interview", "Paris", "25/04/2024", "30/04/2024", "Pounds Sterling", "900000", "70000", "180000", "350000", "60000", "90000")

    def test_create_advance_request_4(self):
        self.fill_form("Juan Camilo Restrepo", "54321001", "Cédula de ciudadanía", "13/04/2024", "08/05/2024", "Departamento de Finanzas", "Reunión de negocios", "Bogotá", "23/04/2024", "28/04/2024", "Pesos colombianos", "800000", "60000", "150000", "300000", "50000", "80000")

    def test_create_advance_request_5(self):
        self.fill_form("María Fernanda Gómez", "98765001", "Cédula de extranjería", "16/04/2024", "11/05/2024", "Departamento de Recursos Humanos", "Entrevista de trabajo", "Medellín", "26/04/2024", "01/05/2024", "Pesos colombianos", "700000", "55000", "130000", "250000", "45000", "75000")

    def test_create_advance_request_6(self):
        self.fill_form("Luisa Sánchez", "1122334455", "Cédula de ciudadanía", "19/04/2024", "14/05/2024", "Departamento de Marketing", "Presentación en conferencia", "Cali", "29/04/2024", "04/05/2024", "Pesos colombianos", "850000", "70000", "160000", "280000", "60000", "90000")

    def test_create_advance_request_7(self):
        self.fill_form("Andrés López", "9988776655", "Cédula de ciudadanía", "22/04/2024", "17/05/2024", "Departamento de Tecnología", "Capacitación en tecnologías emergentes", "Cartagena", "02/05/2024", "07/05/2024", "Pesos colombianos", "750000", "60000", "140000", "270000", "55000", "85000")

    def test_create_advance_request_8(self):
        self.fill_form("Camila Martínez", "3344556677", "Cédula de ciudadanía", "25/04/2024", "20/05/2024", "Departamento de Logística", "Visita a proveedores", "Bucaramanga", "05/05/2024", "10/05/2024", "Pesos colombianos", "900000", "65000", "170000", "320000", "65000", "100000")

    def test_create_advance_request_9(self):
        self.fill_form("José Rodríguez", "1122334455", "Cédula de ciudadanía", "28/04/2024", "23/05/2024", "Departamento de Ventas", "Negociación con clientes", "Pereira", "08/05/2024", "13/05/2024", "Pesos colombianos", "800000", "60000", "150000", "300000", "50000", "80000")

    def test_create_advance_request_10(self):
        self.fill_form("Laura Pérez", "9988776655", "Cédula de ciudadanía", "01/05/2024", "26/05/2024", "Departamento de Investigación y Desarrollo", "Presentación de resultados de investigación", "Manizales", "11/05/2024", "16/05/2024", "Pesos colombianos", "700000", "55000", "130000", "250000", "45000", "75000")

    def test_create_advance_request_11(self):
        self.fill_form("Carlos Gutiérrez", "3344556677", "Cédula de ciudadanía", "04/05/2024", "29/05/2024", "Departamento de Calidad", "Auditoría interna", "Cúcuta", "14/05/2024", "19/05/2024", "Pesos colombianos", "850000", "70000", "160000", "280000", "60000", "90000")

    def test_create_advance_request_12(self):
        self.fill_form("Isabella Hernández", "1122334455", "Cédula de ciudadanía", "07/05/2024", "01/06/2024", "Departamento Legal", "Reunión con abogados externos", "Ibagué", "17/05/2024", "22/05/2024", "Pesos colombianos", "750000", "60000", "140000", "270000", "55000", "85000")

    def test_create_advance_request_13(self):
        self.fill_form("Daniel Ramírez", "9988776655", "Cédula de ciudadanía", "10/05/2024", "05/06/2024", "Departamento de Compras", "Visita a feria internacional", "Santa Marta", "20/05/2024", "25/05/2024", "Pesos colombianos", "900000", "65000", "170000", "320000", "65000", "100000")

    def test_create_advance_request_14(self):
        self.fill_form("Valentina Gómez", "3344556677", "Cédula de ciudadanía", "13/05/2024", "08/06/2024", "Departamento de Recursos Humanos", "Entrevistas de selección", "Pasto", "23/05/2024", "28/05/2024", "Pesos colombianos", "800000", "60000", "150000", "300000", "50000", "80000")

    def test_create_advance_request_15(self):
        self.fill_form("Santiago Morales", "1122334455", "Cédula de ciudadanía", "16/05/2024", "11/06/2024", "Departamento de Finanzas", "Reunión con entidades financieras", "Tunja", "26/05/2024", "31/05/2024", "Pesos colombianos", "700000", "55000", "130000", "250000", "45000", "75000")



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
