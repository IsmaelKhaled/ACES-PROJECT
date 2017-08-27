from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if profile_form.is_valid():
                user.profile.phone_number = profile_form.cleaned_data.get('phone_number')
                user.profile.save()
            logout(request)
            return redirect('login')
    else:
        user_form = SignupForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'form': user_form})
    