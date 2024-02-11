# the form class to describe the forms coming into the application backend from the frontend. this is the DTO of django
from django import forms
from .models import Member

class MemberForm (forms.ModelForm):
 # now we discribe our member form through a Meta class
 class Meta:
  # define model type
  model = Member
  fields = ['fname', 'lname', 'email', 'password', 'age']

# then we will import this form.py file in the views.py file