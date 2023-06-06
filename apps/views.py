from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.serializers import CategorySerializer, ProductSerializer
from apps.models import Product, Category
from rest_framework import viewsets
from django_filters import rest_framework as filters
from apps.filter import ProductFilter

category_id = openapi.Parameter('category_id', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_INTEGER)

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        manual_parameters=[category_id],
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if 'category_id' in request.query_params:
            category_id = request.query_params['category_id']
            queryset = queryset.filter(category_id=category_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
