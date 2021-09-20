from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request, 'home.htm')
    
def about(request):
    return render(request, 'about.htm')

def contact(request):
    return render(request, 'contact.htm')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.htm')

def login(request):
    error = ""
    if request.method == "POST":
        username_a = request.POST['uname']
        password_a = request.POST['pwd']
        user = authenticate(username = username_a,password = password_a)
        try :
            if user.is_staff:
                login(request,user)
                error = 'No'
            else:
                error = "Yes"
        except:
            error = "Yes"
    d = {'error':error}
    return render(request,'login.htm', d )

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

