from django import forms
from django.contrib.auth.models import User
from authapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

# class UserProfileInfo(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ''


# class SignUp(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     #password = forms.PasswordInput()