from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length = 11,required = True, help_text = 'Your Phone Number. XXXXXXXXXXX')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        labels = {'username': ('E-Mail'),}
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('phone_number',)