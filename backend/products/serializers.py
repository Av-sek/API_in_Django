from api.serializers import UserPublicSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title_no_hello,unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
        )
    title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title])
    class Meta:
        model = Product
        fields = [
            'pk',
            'owner',
            'edit_url',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'public'
        ]
    def get_my_user_data(self,obj):
        return {
            "username": obj.user.username
        }
    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse(
            "product-edit",
            kwargs={'pk':obj.id},
            request=request
            )

