from django.shortcuts import render
from .models import UserModel, DoggyDetails, SitterDetails
from django.http import HttpResponse
from django.conf import settings

def index(request):
    return render(request, 'home2.html')


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
        Title = 'Dog Sitter'

    else:
        for sitter in UserModel.objects.filter(babysitter=True):
            for details in SitterDetails.objects.filter(usermodel__email=sitter.email):
                JobListing[sitter.__str__] = {
                    'name' : sitter.__str__, 
                    'location' : sitter.location, 
                    'intro' : sitter.intro,
                    'description' : sitter.description,
                    'photo' : sitter.photo 
                }
        Title = 'Dog Owner'
    
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
            intro = request.POST['intro']
            description = request.POST['description']
            location = request.POST['location']
            photo = request.POST['photo']
            user.save()
            sitter = SitterDetails(usermodel=user, price=price , intro=intro, description=description, location=location, photo=photo)
            sitter.save()

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
            return render(request , 'doggyPage.html', doggyDetails)

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
            return render(request , 'doggy_page.html', get_data(username))
        else:
            return render(request , 'doggyPage.html', get_data(username))
        
    else:
        return render(request , 'login.html')

