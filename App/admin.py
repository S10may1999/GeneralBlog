from django.contrib import admin
from .models import blobmodel
# Register your models here.


@admin.register(blobmodel)
class Adminblog(admin.ModelAdmin):
    list_display=['id','title','desc']