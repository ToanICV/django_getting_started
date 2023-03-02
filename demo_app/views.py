from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Responser
from .serializers import demo_serializer
from rest_framework.response import Response

# Create your views here.
class GetHandler(APIView):
    def get(self, request):
        list_response = Responser.objects.all()
        data_response = demo_serializer(list_response, many=True)
        # return JsonResponse({'message': "You call get"}, status=status.HTTP_200_OK)
        return Response(data=data_response.data, status=status.HTTP_200_OK)

    