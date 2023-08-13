from django.db import models


class SupportTicket(models.Model):
    request = models.OneToOneField('service_requests.ServiceRequest', on_delete=models.CASCADE)
    response = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
