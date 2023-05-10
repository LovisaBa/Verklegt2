from django.forms import ModelForm, widgets
from users.models import Profile, Payment


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'Name': widgets.TextInput(attrs={'class': 'form-control'}),
            'PhoneNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'StreetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'HouseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ZipCode': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.Select(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        exclude = []
        widgets = {
            'CardHolder': widgets.TextInput(attrs={'class': 'form-control'}),
            'CardNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ExpDateMonth': widgets.Select(attrs={'class': 'form-control'}),
            'ExpDateYear': widgets.Select(attrs={'class': 'form-control'}),
            'cvv': widgets.NumberInput(attrs={'class': 'form-control'})
        }
