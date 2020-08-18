from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signout(request):
    logout(request)
    return redirect('Registration:Login')

@login_required
def skills(request):
    return render(request,'Details/skills.html')