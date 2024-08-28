from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url="/login/")
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    
    return redirect("/login/?next=%s" % request.path)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')

    return redirect("/login/?next=%s" % request.path)