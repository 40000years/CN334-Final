from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from product_management.models import Category, Product
from product_management.serializers import CategorySerializer, ProductSerializer
from django.contrib.auth.models import User
from django.core.management import call_command

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


class CreateSuperuserView(APIView):
    authentication_classes = []  # ยกเว้น authentication
    permission_classes = []      # ยกเว้น permission
    def get(self, request):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            return Response({"message": "Superuser created"})
        return Response({"message": "Superuser already exists"})
class CollectStaticView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        call_command('collectstatic', '--noinput')
        return Response({"message": "Static files collected"})
