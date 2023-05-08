from django.forms import ModelForm, widgets
from users.models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'PhoneNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'StreetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'HouseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'ZipCode': widgets.NumberInput(attrs={'class': 'form-control'}),
            'City': widgets.TextInput(attrs={'class': 'form-control'}),
            'Country': widgets.Select(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'})
        }
