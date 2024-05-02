from django.test import TestCase
from django.urls import reverse

from ..models import ChargeAccountRequest, RequestStatus
from users_mgmt.models import CustomUser as User

class AssignReviewerTestCase(TestCase):
    def setUp(self):
        # Create a user Admin
        self.user = User.objects.create(
            first_name="John",
            last_name="Doe",
            phone="12345678",
            id_type="CC",
            id_number="123456789",
            username="123456789",
            email="john@gmail.com",
            password="testpassword",
            role="admin",
        )

        self.client.force_login(self.user)

        self.user = User.objects.create(
            first_name="Ale",
            last_name="aa",
            phone="12345678",
            id_type="CC",
            id_number="123",
            username="123",
            email="john@gmail.com",
            password="testpassword",
            role="reviewer",
        )
        RequestStatus.objects.create(status="In progress")


    def test_get_request(self):
        response = self.client.get(reverse('charge_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests/create_charge_account_request.html')

    def test_post_request(self):
        data = {
            'amount': '100',
            'concept': 'Test concept',
            'city': 'Test city',
            'date': '2024-04-01',
            'bank_name': 'Test bank',
            'account_type': 'Test type',
            'account_number': 'Test number',
            'cex_no': 'Test cex',
            'rent_tax_declarant': True,
            'fiscal_resident': False,
            'checkbox_choices': 'Test choice',
        }
        response = self.client.post(reverse('charge_account'), data=data)
        self.assertEqual(response.status_code, 302)  # 302 because of redirect
        self.assertEqual(ChargeAccountRequest.objects.count(), 1)
        charge_request = ChargeAccountRequest.objects.first()


    def test_assign_reviewer_exist(self):
        # Obtener el revisor con el nombre de usuario "123"
        reviewer = User.objects.get(username="123")

        # Enviar una solicitud de cuenta de cobro
        data = {
            'amount': '100',
            'concept': 'Test concept',
            'city': 'Test city',
            'date': '2024-04-01',
            'bank_name': 'Test bank',
            'account_type': 'Test type',
            'account_number': 'Test number',
            'cex_no': 'Test cex',
            'rent_tax_declarant': True,
            'fiscal_resident': False,
            'checkbox_choices': 'Test choice',
        }
        self.client.post(reverse('charge_account'), data=data)

        # Obtener la solicitud de cuenta de cobro creada
        charge_request = ChargeAccountRequest.objects.first()

        # Asignar el revisor a la solicitud de cuenta de cobro
        charge_request.reviewer = reviewer
        charge_request.save()

        # Verificar que el revisor fue asignado correctamente
        self.assertEqual(charge_request.reviewer, reviewer)
    def test_post_request_non_existing_user(self):
        # Intentar enviar una solicitud de cuenta de cobro para un usuario que no existe
        data = {
            'amount': '200',
            'concept': 'Test concept for non existing user',
            'city': 'Test city',
            'date': '2024-04-01',
            'bank_name': 'Test bank',
            'account_type': 'Test type',
            'account_number': 'Test number',
            'cex_no': 'Test cex',
            'rent_tax_declarant': True,
            'fiscal_resident': False,
            'checkbox_choices': 'Test choice',
            'user_id': 999,  # ID de usuario que no existe
        }
        response = self.client.post(reverse('charge_account'), data=data)


        # Verificar que el revisor asignado es nulo
        charge_request = ChargeAccountRequest.objects.first()
        self.assertIsNone(charge_request.reviewer)

