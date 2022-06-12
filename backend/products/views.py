
from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer




        
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = None
        serializer.save(content = content)
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self,instance):
        #instance
        super().perform_destroy(instance)
    
#Authentication
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
product_mixin_view = ProductMixinView.as_view()
# @api_view(['GET','POST'])
# def product_alt_view(request,pk=None,*args,**kwargs):
#     method = request.method
    
#     if method=="GET":
#         if pk is not None:
#             obj = get_object_or_404(Product,pk=pk)
#             data = ProductSerializer(obj,many=False).data
#             return Response(data)
#         #list view
#         qs = Product.objects.all()
#         data = ProductSerializer(qs,many=True).data
#         return Response(data)
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save(user=self.request.user)
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = None
#             serializer.save(content = content)
#         return Response(serializer.data)
#     return Response({'invalid':'not good data'},status=400)
                