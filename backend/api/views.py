from email import header
from products.models import Product
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
import json
# Create your views here.
def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data,fields=['id','title','price'])
    return HttpResponse(data,headers={'content-type':"application/json"})
