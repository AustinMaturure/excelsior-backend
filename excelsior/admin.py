from django.contrib import admin
from .models import Articles, Category, Staff, Images

# Register your models here.
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(Articles)
admin.site.register(Images)