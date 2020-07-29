from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ExtUser
# Create your views here.
def signup(request):
    if request.method == "POST":
        if User.objects.filter(username = request.POST['username']).count() == 0:
            if request.POST['password1'] == request.POST['password2']:
                user = User(username = request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password1'])
                user.save()
                extuser = ExtUser(username = user, gender = request.POST['gender'], mobile = request.POST['mobile'], dob = request.POST['dob'], category = request.POST['talent'])
                extuser.save()
                return redirect('Registration:Login')
            else:
                context={'error':"Password and Re-type Password doesn't match!"}
        else:
            context = {'error':"Username already exists!"}
    else:
        context = {}
    return render(request,'Registration/signup.html',context=context)

def loginpage(request):
    return render(request,'Registration/Login.html')
