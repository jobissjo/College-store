from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("store:detail")
        else:
            messages.info(request, "Username or password is invalid")
            return redirect("authentication:login")
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect("authentication:register")
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, "User Created")
                user.save()
                return redirect("authentication:login")
        else:
            messages.warning(request, 'Password not matched')
            return redirect("authentication:register")
    return render(request, 'register.html')
