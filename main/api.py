
from  rest_framework.response import Response
from .models import customer
from .serializers import CustomerSerializer
from rest_framework.decorators import api_view
@api_view(['GET'])
def customerapi(request):
    customers= customer.objects.all()
    data=CustomerSerializer(customers,many=True).data
    return Response({'data':data})