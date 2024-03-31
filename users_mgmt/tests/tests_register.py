from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser as User


class UserRegistrationTestCase(TestCase):

    def test_user_registration_success(self):
        # Test user data
        first_name = ("John",)
        last_name = ("Doe",)
        phone = ("12345678",)
        id_type = ("CC",)
        id_number = ("123456789",)
        email = ("john@gmail.com",)
        password = ("testpassword",)

        # Send a POST request to the register view with the user data
        response = self.client.post(
            reverse("register"),
            {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "id_type": id_type,
                "id_number": id_number,
                "email": email,
                "password": password,
                "password_confirm": password,
            },
        )

        # Verify that the user was redirected to the home page
        self.assertEqual(response.status_code, 302)

        # Verify that the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_registration_failure(self):
        # Test user data
        first_name = ("John",)
        last_name = ("Doe",)
        phone = ("12345678",)
        id_type = ("CC",)
        id_number = ("123456789",)
        email = ("jhon@gmail.com",)
        password = ("testpassword",)

        # Send a POST request to the register view with invalid data
        response = self.client.post(
            reverse("register"),
            {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "id_type": id_type,
                "id_number": id_number,
                "email": email,
                "password": password,
                "password_confirm": "wrongpassword",
            },
        )

        # Verify that the user was not redirected to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_registration_get(self):
        # Send a GET request to the register view
        response = self.client.get(reverse("register"))

        # Verify that the user was not redirected to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
