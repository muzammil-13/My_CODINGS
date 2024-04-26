from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken 👎")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken 👎")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                fname=fname,
                                                lname=lname,
                                                email=email)
                user.save()
                print("USER REGISTERED!!")
        else:
            messages.info(request, "Passwords not matching 🚫")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
