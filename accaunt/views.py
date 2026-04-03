from django.contrib.auth import authenticate
from django.contrib import auth ,messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect
from django.shortcuts import render
from .forms import UserUpdateForm, ProfileUpdateForm, SignUpForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username yoki parol xato ')
            return redirect('/accaunt/login/')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form
        }
    return render(request, 'profile_edit.html', context)




def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


