from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignupForm, ProfilePictureForm, ProfileBannerForm
from .models import Profile


# @login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        if request.method == 'POST':
            form_type = request.POST.get('form_type')
            if form_type == 'avatar':
                form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile', pk=pk)
            elif form_type == 'banner':
                form = ProfileBannerForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('profile', pk=pk)
        else:
            form = ProfilePictureForm(instance=profile)
        return render(request, 'user/profile.html', {"profile": profile, "form": form})
    else:
        return redirect('login')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            ''' АВТОРИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ '''
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('mainpage')

    return render(request, 'user/register.html')
