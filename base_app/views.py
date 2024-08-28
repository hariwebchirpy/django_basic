from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    
    return render(request,'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'index.html')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return render(request,'index.html')


