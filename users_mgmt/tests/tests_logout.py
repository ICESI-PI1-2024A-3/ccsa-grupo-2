from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser as User


class UserLogoutTestCase(TestCase):

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

    def test_user_logout(self):
        # Send a POST request to the login view with the user credentials
        self.client.login(username="123456789", password="testpassword")
        response = self.client.get(reverse("logout"))

        # Verify that the user was redirected to the login page
        self.assertEqual(response.status_code, 302)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user_logout_not_authenticated(self):
        # Send a GET request to the logout view
        response = self.client.get(reverse("logout"))

        # Verify that the user was redirected to the login page
        self.assertEqual(response.status_code, 302)

        # Verify that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
