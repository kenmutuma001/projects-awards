from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# from pyuploadcare.dj.forms import FileWidget
# from pyuploadcare.dj.models import ImageField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'image', 'description', 'link')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']

class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = ['rating',]

class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating', ]

class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignRating
        fields = ['rating', ]
        
class ProfileUpdateForm(forms.ModelForm):
   '''
   Profile update form. 

   Allows user to add a bio and a custom avatar.
   '''

   class Meta:
      model = Profile
      fields = ['prof_pic','bio']
      widgets = {
         'bio': forms.Textarea(attrs={'placeholder': 'Bio'})         
      }

class UserUpdateForm(forms.ModelForm):
   '''
   User update form.

   A user can add their name
   '''
   first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
   last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
   class Meta:
      model = User
      fields = ['first_name','last_name']
        