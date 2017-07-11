from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from neighborhoodwatch.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.contact_email = form.cleaned_data.get('contact_email')
            user.profile.contact_phone = form.cleaned_data.get('contact_phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
