from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
from .models import Blog, HeroImage, Imprint, LastProduct, Poem, Product
from .serializers import (
    HeroImageSerializer,
    LastProductSerializer,
    PoemSerializer,
    ProductSerializer,
    BlogSerializer,
    ImprintSerializer,
)


class ProductListDe(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Only return events where enabled is True
        return Product.objects.filter(language="de")

    def list(self, request, *args, **kwargs):
        # Call the parent method to get the default response
        response = super().list(request, *args, **kwargs)

        # Modify the response data to wrap it in a custom key
        return Response({"products": response.data})


class ProductListEn(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Only return events where enabled is True
        return Product.objects.filter(language="en")

    def list(self, request, *args, **kwargs):
        # Call the parent method to get the default response
        response = super().list(request, *args, **kwargs)

        # Modify the response data to wrap it in a custom key
        return Response({"products": response.data})


class LastProductList(generics.ListAPIView):
    queryset = LastProduct.objects.all()
    serializer_class = LastProductSerializer


class HeroImageList(generics.ListAPIView):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer


class PoemList(generics.ListAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class ImprintAPI(generics.ListAPIView):
    queryset = Imprint.objects.all()
    serializer_class = ImprintSerializer


class BlogPostListCreateViewDe(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        # Only return events where enabled is True
        return Blog.objects.filter(language="de")

    def list(self, request, *args, **kwargs):
        # Call the parent method to get the default response
        response = super().list(request, *args, **kwargs)

        # Modify the response data to wrap it in a custom key
        return Response({"blogs": response.data})


class BlogPostListCreateViewEn(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        # Only return events where enabled is True
        return Blog.objects.filter(language="en")

    def list(self, request, *args, **kwargs):
        # Call the parent method to get the default response
        response = super().list(request, *args, **kwargs)

        # Modify the response data to wrap it in a custom key
        return Response({"blogs": response.data})
