from django.contrib import admin
from .models import UserModel, DoggyDetails, SitterDetails
# Register your models here.
admin.site.register(UserModel)
admin.site.register(DoggyDetails)
admin.site.register(SitterDetails)