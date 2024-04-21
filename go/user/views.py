
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreationForm, UserLoginForm
from .models import User


# def authenticate(phone_number=None, password=None, **kwargs):
#     from django.contrib.auth import get_user_model
#     usermodel = get_user_model()
#     if phone_number is None:
#         username = kwargs.get(usermodel.USERNAME_FIELD)
#     try:
#         user = usermodel._default_manager.get_by_natural_key(phone_number)
#         if user.check_password(password):
#             return user
#     except usermodel.DoesNotExist:
#         # Run the default password hasher once to reduce the timing
#         # difference between an existing and a non-existing user (#20760).
#         usermodel().set_password(password)

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('article:home')
            else:
                raise ValueError("Пользователя не существует!")
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
   if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('user:login')
   else:
       form = UserCreationForm()

   return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('article:home')

