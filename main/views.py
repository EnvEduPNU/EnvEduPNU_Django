from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class main(APIView):
    def get(self, request):
        return Response('Get Response')

    def post(self, request):
            # Return an error response if the request is not a valid POST request or no 'image' file is found
        return Response('Post Response')

