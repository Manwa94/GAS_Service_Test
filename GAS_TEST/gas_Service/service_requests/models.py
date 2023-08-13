from django.db import models


class ServiceRequest(models.Model):
    TYPES = (('Gas Booking', 'Gas Leak'),('Meter Installation', 'Meter Deinstallation'),)
        # Add more types as needed

    status = models.CharField(max_length=20, default='Pending')
    type = models.CharField(max_length=50, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
