from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from product_management.models import Product
from product_management.serializers import ProductSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        qs = Product.objects.all()

        province = request.query_params.get("province")
        if province:
            qs = qs.filter(address__iexact=province)

        serializer = ProductSerializer(qs, many=True)
        return Response({"data": serializer.data}, status=200)


class ProductDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_id, format=None):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product)
            return Response({"data": serializer.data})
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

class ProductCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

class CategoryCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer