

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# Create your views here.
@api_view(['POST'])
def api_home(request,*args,**kwargs):
    """Drf Api View"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({'invalid':'not good data'},status=400)