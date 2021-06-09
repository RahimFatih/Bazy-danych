import datetime
from django import forms
from .models import Machines, WorkerPosition, Personaldata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from fieldmaker.form import ExpandableFrom, ExpandableModelForm


def machines():
    choices = []
    for each in Machines.objects.all():
        choices.append((each.id_machine, each.name))

    return choices

def worker_position():
    choices = []
    for each in WorkerPosition.objects.all():
        choices.append((each.id_worker_position, each.worker_position_type))

    return choices

def workers():
    choices = []
    for each in Personaldata.objects.all():
        choices.append((each.id, each.name+" "+each.surname))

    return choices

type_choices = (
    ("Awaria całkowita","Awaria całkowita"),
    ("Usterka", "Usterka"),
    ("Kolizja", "Kolizja"),
    ("Inny", "Inny")
    )

lic_choices = (
    ("Office 360", "Office 360"),
    ("Norton", "Norton"),
    ("Jira", "Jira")
)

class Report(forms.Form):

    reporting_worker = forms.ChoiceField(choices = workers(), label="Pracownik zgłaszający")
    report_date = forms.DateTimeField(initial=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    machine = forms.ChoiceField(choices = machines(), label = "Maszyna ",)
    damage_type = forms.ChoiceField(choices = type_choices, label= "Typ Awarii")
    description = forms.CharField(max_length=255, label="Opis problemu")

class SignUpWorker(forms.Form):
    name = forms.CharField(max_length=255, help_text="Wymagane.")
    surname = forms.CharField(max_length=255, help_text="Wymagane.")
    birthday = forms.DateField(initial=datetime.datetime.now().strftime("%Y-%m-%d"))
    gender = forms.ChoiceField(choices= (( "female", "Kobieta"),("male", "Mężczyzna")))
    position = forms.ChoiceField(choices=worker_position(), help_text="Wymagane.")
    licenses = forms.MultipleChoiceField(choices=lic_choices)


class ResolveReport(forms.Form):

    resolve_date = forms.DateTimeField(initial=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))