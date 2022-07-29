from itertools import product
from rest_framework import mixins,viewsets
from .models import Product
from api.permissions import IsStaffEditorPermission
from .serializers import ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default
    
class ProductGenericViewSet(
    IsStaffEditorPermission,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default
    

# product_list = ProductGenericViewSet.as_view({'get':'list'})

# product_detail = ProductGenericViewSet.as_view({
#     'get':'retrieve'
# })