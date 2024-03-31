from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser as User


class AssignRolesTestCase(TestCase):

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

    def test_assign_roles_success(self):
        # Send a POST request to the assign_roles view with the user data
        response = self.client.post(
            reverse("assign_roles"),
            {
                "user_id": self.user.id,
                "role": "Accounting Manager",
            },
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "Accounting Manager")

    def test_assign_roles_invalid_role(self):
        # Send a POST request to the assign_roles view with an invalid role
        response = self.client.post(
            reverse("assign_roles"),
            {
                "user_id": self.user.id,
                "role": "invalid_role",
            },
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was not updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "requester")

    def test_assign_roles_invalid_user(self):
        # Send a POST request to the assign_roles view with an invalid user id
        response = self.client.post(
            reverse("assign_roles"),
            {
                "user_id": "invalid_id",
                "role": "Accounting Manager",
            },
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was not updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "requester")

    def test_assign_roles_missing_user_id(self):
        # Send a POST request to the assign_roles view without a user id
        response = self.client.post(
            reverse("assign_roles"),
            {
                "role": "Accounting Manager",
            },
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was not updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "requester")

    def test_assign_roles_missing_role(self):
        # Send a POST request to the assign_roles view without a role
        response = self.client.post(
            reverse("assign_roles"),
            {
                "user_id": self.user.id,
            },
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was not updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "requester")

    def test_assign_roles_missing_user_id_and_role(self):
        # Send a POST request to the assign_roles view without a user id and role
        response = self.client.post(
            reverse("assign_roles"),
            {},
        )

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)

        # Verify that the user role was not updated
        self.assertEqual(User.objects.get(pk=self.user.id).role, "requester")

    def test_assign_roles_get(self):
        # Send a GET request to the assign_roles view
        response = self.client.get(reverse("assign_roles"))

        # Verify that the user was redirected to the assign_roles page
        self.assertEqual(response.status_code, 200)
