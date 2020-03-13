from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Task)
admin.site.register(ProductType)
admin.site.register(ProductSubType)
admin.site.register(Product)
admin.site.register(Cart)