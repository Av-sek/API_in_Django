from django.urls import path

from . import views

urlpatterns = [
    path('',views.product_mixin_view),
    path('<int:pk>/',views.product_mixin_view),
    path('update/<int:pk>/',views.ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>/',views.ProductDeleteAPIView.as_view()) 
    
]
