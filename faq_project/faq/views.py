from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [
            {"id": faq.id, **faq.get_translation(lang)}
            for faq in faqs
        ]
        return Response(data, status=status.HTTP_200_OK)
