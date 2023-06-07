from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MachineLearning(APIView):
    def get(self, request):
        return Response('Get MachineLearning Response')

    def post(self, request):
            # Return an error response if the request is not a valid POST request or no 'image' file is found
        return Response('Post MachineLearning Response')