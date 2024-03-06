from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.api.selector.api_selector import ApiSelector

class ApiController(APIView):
    def get(self,request):
        data=ApiSelector.getData()
        return Response({"data":data},status=status.HTTP_200_OK)