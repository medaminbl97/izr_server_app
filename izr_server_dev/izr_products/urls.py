from django.urls import path
from .views import (
    BlogPostListCreateViewEn,
    BlogPostListCreateViewDe,
    HeroImageList,
    LastProductList,
    PoemList,
    ProductListDe,
    ProductListEn,
    ImprintAPI,
)

urlpatterns = [
    path("products/de", ProductListDe.as_view(), name="product-list-de"),
    path("products/en", ProductListEn.as_view(), name="product-list-en"),
    path("last_product/", LastProductList.as_view(), name="last-product-list"),
    path("poem/", PoemList.as_view(), name="poem"),
    path("hero/", HeroImageList.as_view(), name="hero-image"),
    path("imprint/", ImprintAPI.as_view(), name="imprint"),
    path("blog/en", BlogPostListCreateViewEn.as_view(), name="blog-post-list-en"),
    path("blog/de", BlogPostListCreateViewDe.as_view(), name="blog-post-list-de"),
]
