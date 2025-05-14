from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

# View สำหรับหน้าเว็บ
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # วนกลับมาหน้าเดิม (หรือเปลี่ยนเป็น product_list ถ้ามี)
    else:
        form = ProductForm()
    return render(request, 'product_management/add_product.html', {'form': form})

# View สำหรับ API
class ProductCreateAPI(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# View จาก urls.py เดิม
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'