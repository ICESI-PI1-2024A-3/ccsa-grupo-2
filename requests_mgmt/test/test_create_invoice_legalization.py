from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import InvoiceLegalizationRequest, RequestStatus

class InvoiceLegalizationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_get_request(self):
        response = self.client.get(reverse('invoice_legalization'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requests/create_invoice_legalization_request.html')

    def test_post_request(self):
        data = {
            'legalization_date': '2024-04-01', 
            'dependency': 'Test dependency',
            'destination_city': 'Test city',
            'departure_date': '2024-04-02',  
            'reason_trip': 'Test reason',
            'autorizar_descuento': 'Test authorization',
            'bank_name': 'Test bank',
            'account_type': 'Test type',
            'account_number': 'Test number',
        }
        response = self.client.post(reverse('invoice_legalization_view'), data=data)
        self.assertEqual(response.status_code, 302)  # 302 because of redirect
        self.assertEqual(InvoiceLegalizationRequest.objects.count(), 1)
        invoice_request = InvoiceLegalizationRequest.objects.first()
        self.assertEqual(invoice_request.legalization_date, '2024-04-01')
        self.assertEqual(invoice_request.dependency, 'Test dependency')
        

   