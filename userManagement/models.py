from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    babysitter = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class DoggyDetails(models.Model):
    usermodel = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    nature = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'pics')

    def __str__(self):
        return self.name

class SitterReq(models.Model):
    usermodel = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    duration = models.IntegerField()
    


