from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import *
from .models import *
from .decorators import *
# Create your views here.


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    content={}
    return render(request, "registration/login.html", content)

def logoutUser(request):
    logout((request))
    return redirect('login')


@login_required(login_url='login')
def home(response):
    return render(response, "main/home.html", {})

# @login_required(login_url='login')
def report(response):
    forms = Report()
    return render(response, "main/report.html", { "forms": forms })

# @login_required(login_url='login')
def report_view(response, pk):
    report = Crashreport.objects.get(id_crash_report=pk)
    return render(response, "main/report_view.html", {'report': report})

# @login_required(login_url='login')
def report_list(response):
    reports = Crashreport.objects.all()
    machines = Machines.objects.all()
    return render(response, "main/report_list.html", {'reports':reports, 'machines':machines})