from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
]