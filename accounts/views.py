import email
from django.contrib.auth.models import User ,auth
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email'] 
        if password1 != password2:
            messages.info(request ,'Password Does not match')
            return redirect('register')
        elif User.objects.filter(username = username).exists():
            messages.info(request ,'Username taken') 
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request ,'email already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username ,password = password1, email = email , first_name = first_name , last_name = last_name ,  )
            user.save()
            return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        lusername =request.POST['lusername']
        lpassword =request.POST['lpassword']
        user = auth.authenticate(username = lusername , password = lpassword)
        if user is not None:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request ,'Invalid Credientials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')