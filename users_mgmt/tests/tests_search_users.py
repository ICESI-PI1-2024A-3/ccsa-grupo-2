from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser as User


class SearchUsersTestCase(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            phone="12345678",
            id_type="CC",
            id_number="123456789",
            username="123456789",
            email="john@gmail.com",
            password="testpassword",
        )

        self.client.force_login(self.user)

    def test_search_users_success(self):
        # Send a GET request to the search_users view
        response = self.client.get(reverse("search_users"), {"search_query": "John"})

        # Verify that the user was redirected to the search_users page
        self.assertEqual(response.status_code, 200)

        # Verify that there is response context
        self.assertIn("users_and_forms", response.context)

    def test_search_users_no_results(self):
        # Send a GET request to the search_users view
        response = self.client.get(reverse("search_users"), {"search_query": "Jane"})

        # Verify that the user was redirected to the search_users page
        self.assertEqual(response.status_code, 200)

        # Verify that there is not response context
        self.assertNotIn("users_and_forms", response.context)

    def test_search_users_no_query(self):
        # Send a GET request to the search_users view
        response = self.client.get(reverse("search_users"))

        # Verify that the user was redirected to the search_users page
        self.assertEqual(response.status_code, 200)

        # Verify that there is response context
        self.assertIn("users_and_forms", response.context)
