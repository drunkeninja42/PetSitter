from django.shortcuts import render
from .models import UserModel, DoggyDetails, SitterReq
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'index.html')


def get_data(username):
    user = UserModel.objects.get(username=username)
    UserData = {}
    UserData['first_name'] = user.first_name
    UserData['last_name'] = user.last_name
    UserData['username'] = user.username
    UserData['password'] = user.password
    UserData['email'] = user.email
    UserData['babysitter'] = user.babysitter

    JobListing = {}
    Title = ''
    if user.babysitter:
        for seeker in UserModel.objects.filter(babysitter=False):
            for dog in DoggyDetails.objects.filter(usermodel__email=seeker.email):
                JobListing[dog.name] = {
                    'name' : dog.name, 
                    'breed' : dog.breed, 
                    'nature' : dog.nature, 
                    'photo' : dog.photo 
                }
        Title = 'Babysitter'

    else:
        for sitter in UserModel.objects.filter(babysitter=True):
            for human in SitterReq.objects.filter(usermodel__email=sitter.email):
                JobListing[sitter.__str__] = {
                    'name' : sitter.__str__, 
                    'price' : human.price, 
                    'duration' : human.duration 
                }
        Title = 'Seeker'
    
    return {'UserData':UserData, 'JobListing':JobListing, 'Title':Title}


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

        if user.babysitter:
            price = request.POST['price']
            duration = request.POST['duration']
            user.save()
            req = SitterReq(usermodel=user, price=price , duration=duration)
            req.save()

            sitterDetails = get_data(user.username)
            return render(request , 'doggy_page.html', sitterDetails)

        else:
            name = request.POST['name']
            breed = request.POST['breed']
            nature = request.POST['nature']
            description = request.POST['description']
            photo = request.POST['photo']
            user.save()
            dog = DoggyDetails(usermodel=user, name=name , breed=breed , nature=nature , description=description , photo=photo)
            dog.save()

            doggyDetails = get_data(user.username)
            return render(request , 'doggy_page.html', doggyDetails)

    else :
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserModel.objects.get(username=username, password=password)
        except:
            return HttpResponse('username or password does not exists.......')

        if user.babysitter:
            doggyDetails = get_data(username)
            return render(request , 'doggyPage.html', doggyDetails)
        else:
            sitterDetails = get_data(username)
            return render(request , 'doggy_page.html', sitterDetails)
        
    else:
        return render(request , 'login.html')

