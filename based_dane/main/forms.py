from django import forms
from .models import Machines
# from fieldmaker.form import ExpandableFrom, ExpandableModelForm


def machines():
    choices = []
    for each in Machines.objects.all():
        choices.append((str(each.id_machine), each.name))

    return choices

type_choices = (
    ("Awaria całkowita","Awaria całkowita"),
    ("Usterka", "Usterka"),
    ("Kolizja", "Kolizja"),
    ("Inny", "Inny")
    )

class Report(forms.Form):

    machine = forms.ChoiceField(choices = machines(), label = "Maszyna ",)
    damage_type = forms.ChoiceField(choices = type_choices, label= "Typ Awarii")
    description = forms.CharField(max_length=255, label="Opis problemu")
