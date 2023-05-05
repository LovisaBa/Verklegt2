from django.forms import ModelForm, widgets
from django import forms
from users.models import Profile


class UserCreateForm(ModelForm):
    image = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        exclude = ['id', 'users']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'PhoneNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'StreetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'HouseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ZipCode': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.Select(attrs={'class': 'form-control'})
        }
