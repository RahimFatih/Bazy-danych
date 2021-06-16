from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

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

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.name = form.cleaned_data.get('name')
#             user.profile.surname = form.cleaned_data.get('surname')
#             user.profile.birthday = form.cleaned_data.get('birthday')
#             user.profile.gender = form.cleaned_data.get('gender')
#             user.profile.position = form.cleaned_data.get('position')
#             user.profile.licenses = form.cleaned_data.get('licenses')

#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'main/signup.html', {'form': form})


def signup(response):
    if response.method == 'POST':
        form = SignUpWorker(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            birthday = form.cleaned_data["birthday"]
            gender = form.cleaned_data["gender"]
            position = WorkerPosition.objects.get(pk = form.cleaned_data["position"])
            licenses = form.cleaned_data["licenses"][0]
            print(licenses)

            print(gender)

            worker = Personaldata(
                name = name,
                surname = surname,
                birthday = birthday,
                gender = gender,
                position = position,
                licenses = licenses
            )
            worker.save()

        return HttpResponseRedirect('../success')

    else:
        form = SignUpWorker()

    return render(response, "main/signup.html", {"form": form})


def logoutUser(request):
    logout((request))
    return redirect('login')


def home(response):
    return render(response, "main/home.html", {})

# @login_required(login_url='login')
def report(request):
    # forms = Report()

    if request.method == 'POST':
        forms = Report(request.POST)

        if forms.is_valid():

            reporting_worker = Personaldata.objects.get(pk=forms.cleaned_data["reporting_worker"])
            report_date = forms.cleaned_data["report_date"]
            machine = Machines.objects.get(pk=forms.cleaned_data["machine"])
            damage_type = forms.cleaned_data["damage_type"]
            description = forms.cleaned_data["description"]
            report = Crashreport(
                reporting_worker = reporting_worker,
                report_date = report_date,
                crashed_machine = machine,
                type = damage_type,
                description = description
            )
            report.save()

        return HttpResponseRedirect('success')

    else:
        forms = Report()

    return render(request, "main/report.html", { "forms": forms })

def success(response):
    return render(response, "main/success.html", {})

# @login_required(login_url='login')
def report_view(response, pk):
    report = Crashreport.objects.get(id_crash_report=pk)

    if response.method == 'POST':
        form = ResolveReport(response.POST)

        if form.is_valid():

            repair_date = form.cleaned_data["resolve_date"]
            report.repair_date = repair_date
            report.save()

        return HttpResponseRedirect(response.path_info)

    else:
        form = ResolveReport()

    return render(response, "main/report_view.html", {'report': report, 'form':form})

# @login_required(login_url='login')
def report_list(response):
    reports = Crashreport.objects.all()
    return render(response, "main/report_list.html", {'reports':reports})