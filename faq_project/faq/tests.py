import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
    assert faq.question == "What is Django?"

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
