from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken 👎")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken 👎")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email)
            user.save()
            print("User registered!")
        else:
            messages.info(request, "password not matching 🚫")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
