from django.shortcuts import render, redirect
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        type = request.POST['type']
        details = request.POST['details']
        attachment = request.FILES.get('attachment')
        service_request = ServiceRequest.objects.create(type=type, details=details, attachment=attachment)
        return redirect('request_detail', request_id=service_request.id)
    return render(request, 'service_requests/submit_request.html')

def request_detail(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'service_requests/request_detail.html', {'service_request': service_request})
