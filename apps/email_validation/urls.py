from django.urls import path
from .views import ResendEmail, ValidateEmail
urlpatterns = [
    path('<str:validation_uuid>/', ValidateEmail.as_view(), name="validate-email"),
    path('resend-email', ResendEmail.as_view(), name="resend-email"),
]
