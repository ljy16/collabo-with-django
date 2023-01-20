from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect()
    else :
        form = CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        # 유저가 존재하는지를 검증하는 Django 내장 모델 폼
        # 사용자가 로그인 폼에 작성한 정보가 유효한지를 검증함.!
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect()
    else:
        form = AuthenticationForm()
    context = {'form':form,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect()