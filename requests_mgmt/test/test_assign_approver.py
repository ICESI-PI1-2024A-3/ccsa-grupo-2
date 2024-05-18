from django.test import TestCase
from django.urls import reverse

from ..models import ChargeAccountRequest, RequestStatus
from users_mgmt.models import CustomUser as User

class AssignApproverTestCase(TestCase):
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
            first_name="Samuel",
            last_name="Ibarra",
            phone="3122",
            id_type="CC",
            id_number="114",
            username="114",
            email="john@gmail.com",
            password="testpassword",
            role="approver",
        )
        RequestStatus.objects.create(status="Reject")

    def test_get_request(self):
        response = self.client.get(reverse('charge_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests/create_charge_account_request.html')

    def test_post_request(self):
        data = {
            'amount': '500',
            'concept': 'Test',
            'city': 'Calatraba',
            'date': '2024-07-07',
            'bank_name': 'Test bank',
            'account_type': 'Test type',
            'account_number': 'Test number',
            'cex_no': 'Test cex',
            'rent_tax_declarant': True,
            'fiscal_resident': False,
            'checkbox_choices': 'Test choice',
        }
    def test_assign_approver_exist(self):
        # Obtener el aprobador con el nombre de usuario "114"
        approver = User.objects.get(username="114")

        # Enviar una solicitud de cuenta de cobro
        data = {
            'amount': '10000',
            'concept': 'Test ',
            'city': 'Test ',
            'date': '2024-04-01',
            'bank_name': 'Test ',
            'account_type': 'Test ',
            'account_number': 'Test ',
            'cex_no': 'Test cex',
            'rent_tax_declarant': True,
            'fiscal_resident': False,
            'checkbox_choices': 'Test choice',
        }
        self.client.post(reverse('charge_account'), data=data)

        # Obtener la solicitud de cuenta de cobro creada
        charge_request = ChargeAccountRequest.objects.first()

        # Asignar el aprobador a la solicitud de cuenta de cobro
        charge_request.approver = approver
        charge_request.save()

        # Verificar que el aprobador fue asignado correctamente
        self.assertEqual(charge_request.approver, approver)

    def test_post_request_non_existing_user(self):
        # Enviar una solicitud de cuenta de cobro
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
        self.client.post(reverse('charge_account'), data=data)

        # Obtener la solicitud de cuenta de cobro creada
        charge_request = ChargeAccountRequest.objects.first()

        # Verificar que charge_request no es None
        self.assertIsNotNone(charge_request)

        # Verificar que charge_request.approver es None
        self.assertIsNone(charge_request.approver)