from django.urls import path
from . import views

urlpatterns = [
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('create_ticket/<int:request_id>/', views.create_ticket, name='create_ticket'),
]
