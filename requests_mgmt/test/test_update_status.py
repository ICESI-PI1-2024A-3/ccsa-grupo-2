from django.test import TestCase
from django.urls import reverse
from requests_mgmt.models import Request, RequestStatus
from users_mgmt.models import CustomUser

class RequestStatusUpdateTestCase(TestCase):
    def setUp(self):
        # Crear estados de solicitud
        self.pending_status = RequestStatus.objects.create(status='Pendiente de Aceptación')
        self.review_status = RequestStatus.objects.create(status='Revisión')
        self.accepted_status = RequestStatus.objects.create(status='Aceptado')
        self.approved_status = RequestStatus.objects.create(status='Aprobado')
        self.rejected_status = RequestStatus.objects.create(status='Rechazado')

        # Crear usuarios
        self.requester = CustomUser.objects.create_user(email='requester@example.com', password='testpass123')
        self.reviewer = CustomUser.objects.create_user(email='reviewer@example.com', password='testpass123', role='Reviewer')
        self.approver = CustomUser.objects.create_user(email='approver@example.com', password='testpass123', role='Approver')

        # Crear solicitud
        self.request = Request.objects.create(
            type='Cuenta de Cobro',
            status=self.pending_status,
            requester=self.requester
        )

    def test_update_status_to_review(self):
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aceptar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.review_status)

    def test_update_status_to_accepted(self):
        self.request.status = self.review_status
        self.request.reviewer = self.reviewer
        self.request.save()
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aceptar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.accepted_status)

    def test_update_status_to_approved(self):
        self.request.status = self.accepted_status
        self.request.save()
        self.client.login(email=self.approver.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aprobar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.approved_status)

    def test_update_status_to_rejected(self):
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Rechazar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.rejected_status)

    def test_update_status_with_comment(self):
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aceptar', 'comentario': 'Este es un comentario de prueba'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.review_status)
        self.assertEqual(self.request.comments, 'Este es un comentario de prueba')

    def test_update_status_invalid_action(self):
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'InvalidAction'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.pending_status)

    def test_update_status_as_requester(self):
        self.client.login(email=self.requester.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aceptar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.pending_status)

    def test_update_status_to_review_with_reviewer(self):
        self.request.reviewer = self.reviewer
        self.request.save()
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aceptar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.accepted_status)

    def test_update_status_to_approved_with_approver(self):
        self.request.status = self.accepted_status
        self.request.approver = self.approver
        self.request.save()
        self.client.login(email=self.approver.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Aprobar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.approved_status)

    def test_update_status_to_rejected_with_reviewer(self):
        self.request.reviewer = self.reviewer
        self.request.save()
        self.client.login(email=self.reviewer.email, password='testpass123')
        response = self.client.post(reverse('detail_request', args=[self.request.id]), {'action': 'Rechazar'})
        self.assertEqual(response.status_code, 302)
        self.request.refresh_from_db()
        self.assertEqual(self.request.status, self.rejected_status)