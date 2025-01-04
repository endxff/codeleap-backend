import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ItemListCreateView(APIView):
    def get(self, request):
        response = requests.get(f"{settings.EXTERNAL_API_BASE_URL}")
        return Response(response.json(), status=response.status_code)

    def post(self, request):
        response = requests.post(
            f"{settings.EXTERNAL_API_BASE_URL}",
            json=request.data,
            headers={"Content-Type": "application/json"},
        )
        return Response(response.json(), status=response.status_code)


class ItemDetailView(APIView):
    def get(self, request, pk):
        response = requests.get(f"{settings.EXTERNAL_API_BASE_URL}/{pk}/")
        return Response(response.json(), status=response.status_code)

    def patch(self, request, pk):
        response = requests.patch(
            f"{settings.EXTERNAL_API_BASE_URL}/{pk}/",
            json=request.data,
            headers={"Content-Type": "application/json"},
        )
        return Response(response.json(), status=response.status_code)

    def delete(self, request, pk):
        response = requests.delete(f"{settings.EXTERNAL_API_BASE_URL}/{pk}/")
        return Response(response.json(), status=response.status_code)
