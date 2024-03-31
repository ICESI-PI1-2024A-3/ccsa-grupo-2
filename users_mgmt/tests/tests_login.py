from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser as User


class UserLoginTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            phone="12345678",
            id_type="CC",
            id_number="123456789",
            username="123456789",
            email="jhon@gmail.com",
            password="testpassword",
        )

    def test_user_login_success(self):
        # Send a POST request to the login view with the user credentials
        response = self.client.post(
            reverse("login"),
            {
                "username": "123456789",
                "password": "testpassword",
            },
        )

        # Verify that the user was redirected to the home page
        self.assertEqual(response.status_code, 302)

        # Verify that the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_login_failure(self):
        # Send a POST request to the login view with the user credentials
        response = self.client.post(
            reverse("login"),
            {
                "username": "123456789",
                "password": "wrongpassword",
            },
        )

        # Verify that the user was not redirected to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_login_invalid(self):
        # Send a POST request to the login view with invalid data
        response = self.client.post(
            reverse("login"),
            {
                "username": "123456789",
            },
        )

        # Verify that the user was not redirected to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_login_get(self):
        # Send a GET request to the login view
        response = self.client.get(reverse("login"))

        # Verify that the user was not redirected to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
