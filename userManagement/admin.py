from django.contrib import admin
from .models import UserModel,DoggyDetails,SitterReq

# Register your models here.
admin.site.register(UserModel)
admin.site.register(DoggyDetails)
admin.site.register(SitterReq)