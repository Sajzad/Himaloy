from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login
from .forms import UserRegistrationForm
# UserLoginForm

# def LoginView(request):
#     next=request.GET.get('next')
#     form= UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username= form.cleaned_data.get('username')
#         password= form.cleaned_data.get('password')
#         user=authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('index')
#     context= {
#         'form':form
#     }
#     return render(request, 'account/login.html', context)


def RegisterView(request):
    next=request.GET.get('next')
    form= UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user= form.save(commit=False)
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        password1= form.cleaned_data.get('confirm_password')
        user.set_password(password)
        user.save()
        return redirect('login')

    context= {
        'form':form
    }
    return render(request, 'account/signup.html', context)

# def LogOutView(request):
#     logout(request)
#     return redirect('login')
# # Create your views here.
