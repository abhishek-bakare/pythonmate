from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Profile

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2',]



#REPEAT_TYPE= [
#    ('repetition', 'Repetition'),
 #   ('frequency', 'Frequency'),
  #  ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email','start_date', 'start_time', 'end_time','repeat_type','weekdays',]

        labels = {
            'email': ('Email'),
            'start_date': ('Start date'),
            'start_time':('Start time'),
            'end_time':('End time'),
            'repeat_type':('Repeat type'),
            'weekdays':('Weekdays'),

        }

        widgets = {
            'start_date': forms.SelectDateWidget,
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'repeat_type': forms.RadioSelect,
            'weekdays': forms.RadioSelect
        }