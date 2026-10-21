from django import forms
from .models import Event, Team, Cake


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'employee']


class TeamEventForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Выберите команду")
    event = forms.ModelChoiceField(queryset=Event.objects.all(), label="Выберите мероприятие")

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'weight', 'calorie', 'cost']
