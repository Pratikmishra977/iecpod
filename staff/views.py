from django.shortcuts import render, redirect
from .forms import StaffLoginForm
from django.contrib.auth import authenticate, login, logout
from .auth_backends import StaffModelBackend
from .models import Course_Instructor

# Create your views here.

def StaffLogin(request):
    form = StaffLoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Course_Instructor.objects.filter(email=email).exists():
            user =StaffModelBackend().authenticate( username=email, password= password)
            if user is not None and user.is_active:
                login(request, user)
                return render(request,'staff_home.html')
            else:
                return render(request, 'staffLogin.html',{'form': form, 'error_message': 'Wrong Password'})
        else:
            return render(request, 'staffLogin.html', {'form': form, 'error_message': 'User does not exists'})
    else:
        return render(request,'staffLogin.html', {'form': form})


