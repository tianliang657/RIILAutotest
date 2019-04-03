from django.contrib import admin

from apitest.models import Apitest
from product.models import Product


# Register your models here.
class ApitestAdmin(admin.TabularInline):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id', 'product']
    model = Apitest
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'create_time', 'id']
    inlines = [ApitestAdmin]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']  # 后台显示产品模块


admin.site.register(Product, ProductAdmin)
