from django.shortcuts import render
from .models import SupportTicket

def support_dashboard(request):
    tickets = SupportTicket.objects.all()
    return render(request, 'customer_support/support_dashboard.html', {'tickets': tickets})

def create_ticket(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        response = request.POST['response']
        ticket = SupportTicket.objects.create(request=service_request, response=response)
        service_request.status = 'Resolved'
        service_request.resolved_at = ticket.submitted_at
        service_request.save()
    return render(request, 'customer_support/create_ticket.html', {'service_request': service_request})
