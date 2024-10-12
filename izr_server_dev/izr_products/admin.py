from django.contrib import admin
from .models import Blog, ContentItem, HeroImage, LastProduct, Poem, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "language", "price", "amazon_link")


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(LastProduct)
class LastProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amazon_link")


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ("book_name", "content")


class ContentItemInline(admin.TabularInline):
    model = ContentItem
    extra = 1  # How many extra empty fields to display
    fields = ["content_type", "text", "image", "v_image"]
    readonly_fields = ["order"]  # You might want to manually order in the admin


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [ContentItemInline]
    list_display = ("title", "type", "language", "author", "created_at", "updated_at")
    list_filter = ("type", "language")


from django.contrib import admin
from .models import Imprint


@admin.register(Imprint)
class ImprintAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "updated_at",
    )
