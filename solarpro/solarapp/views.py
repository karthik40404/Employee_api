from django.shortcuts import render,redirect

# Create your views here.
def log(req):
    return render(req,'login.html')

def reg(req):
    return render(req,'user/register.html')

def u_home(req):
    return render(req,'user/uhome.html')
