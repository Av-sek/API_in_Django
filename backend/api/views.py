import imp
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# Create your views here.
@api_view(['GET','POST'])
def api_home(request):
    """Drf Api View"""
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data,headers={'content-type':"application/json"})
