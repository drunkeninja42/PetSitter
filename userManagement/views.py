from django.shortcuts import render
from .models import UserModel,DoggyDetails,SitterReq
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST" : 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            request.POST['babysitter']
            user = UserModel(first_name=first_name, last_name=last_name, username=username, password=password, email=email, babysitter=True)
        except:
            user = UserModel(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
        request.session['current_user'] = user.username
        user.save()

        if user.babysitter == True:
            return render(request , 'lena.html')
        else:
            return render(request , 'dena.html')
    else :
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserModel.objects.get(username=username, password=password)
            request.session['current_user'] = user.username

            if user.babysitter == True:
                return render(request , 'lena.html')
            else:
                return render(request , 'dena.html')
        except:
            return HttpResponse('username or password does not exists.......')
    else:
        return render(request , 'login.html')


def dena(request):
    user = UserModel.objects.get(username=request.session['current_user'])
    name = request.POST['name']
    breed = request.POST['breed']
    nature = request.POST['nature']
    description = request.POST['description']
    photo = request.POST['photo']
    dog = DoggyDetails(usermodel=user, name = name , breed = breed , nature = nature , description = description , photo = photo)
    dog.save()
    return HttpResponse('{} {} {} {}'.format(name , breed , nature , description))


def lena(request):
    # if request.method == "POST":
    user = UserModel.objects.get(username=request.session['current_user'])
    price = request.POST['price']
    duration = request.POST['duration']
    req = SitterReq(usermodel=user, price = price , duration = duration)
    req.save()

