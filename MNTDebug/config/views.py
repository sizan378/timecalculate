from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from order.models import OrderModel
from django.shortcuts import get_object_or_404
from config.utils import tokenValidation
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

class UserCheckBalanceView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    """
        It gets the token from the header, send it to tokenvalidation custom func 
        and get payload, extract phone number & query with it the amount from the database
        :param request: The request object
        :return: The amount of the user is being returned.
    """

    def get(self, request):
        payload = tokenValidation(request)

        get_id_no = payload['user_id']
        print(get_id_no)
        amount = get_object_or_404(
            OrderModel, order_id=get_id_no).amount
        return Response({'amount': amount})