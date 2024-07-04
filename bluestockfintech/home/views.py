from django.shortcuts import render, redirect

def home(request):
    # print("Heywe are in home")
    return render(request, 'index12.html')

def dashboard(request):
    return render(request, 'admindash.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def adminforgetpass(request):
    return render(request, 'adminforgetpass.html')

def adminsignin(request):
    return render(request, 'adminsignin.html')