from django.urls import path
from django.urls import path
from .views import SignUpView


URLPatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]