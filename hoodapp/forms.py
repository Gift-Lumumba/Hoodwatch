from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood,Business,Profile,Posts,Comments

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddHoodForm(forms.ModelForm):
  '''
  Form class that enables a user create a neighbourhood
  '''
  class Meta:
    model = Neighbourhood
    fields = ['name','location','description','police_dept','health_dept']
    exclude = ['posted_on']


class AddBusinessForm(forms.ModelForm):
	'''
  Form class that enables a user create a business in the neighbourhood
	'''
	class Meta:
		model = Business
		fields = ['name','email','description']

class UpdateProfileForm(forms.ModelForm):
  '''
  Form class that enables a users update their profiles
  '''
  class Meta:
    model = Profile
    fields = ['bio']

class PostForm(forms.ModelForm):
  '''
  Form class that enables a user post in a neighbourhood
  '''
  class Meta:
    model = Posts
    fields = ['topic','post']