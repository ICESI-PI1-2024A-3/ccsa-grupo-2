from django.test import TestCase
from django.urls import reverse

from ..models import ChargeAccountRequest,Request
from users_mgmt.models import CustomUser

class ChargeAccountTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

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
        self.assertEqual(charge_request.amount, '100')
        self.assertEqual(charge_request.concept, 'Test concept')
