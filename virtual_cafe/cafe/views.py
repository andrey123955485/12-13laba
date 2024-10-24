from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import CustomUserCreationForm

MAX_CAPACITY = 3 # Максимальное количество пользователей в кафе

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cafe/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'cafe/login.html', {'error': 'Неверное имя пользователя или пароль.'})
    return render(request, 'cafe/login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if CustomUser.objects.filter(is_present=True).count() >= MAX_CAPACITY:
        return render(request, 'cafe/full.html')

    users = CustomUser.objects.filter(is_present=True)
    return render(request, 'cafe/home.html', {'users': users})

def order_coffee(request):
    if request.user.is_authenticated:
        request.user.coffee_status = True
        request.user.save()
        return redirect('home')
    else:
        return redirect('login')

def drink_coffee(request):
    if request.user.is_authenticated:
        request.user.coffee_status = False
        request.user.save()
        return redirect('home')
    else:
        return redirect('login')

def enter_cafe(request):
    if request.user.is_authenticated:
        if CustomUser.objects.filter(is_present=True).count() < MAX_CAPACITY:
            request.user.is_present = True
            request.user.save()
            return redirect('home')
        else:
            return render(request, 'cafe/full.html')
    else:
        return redirect('login')

def exit_cafe(request):
    if request.user.is_authenticated:
        request.user.is_present = False
        request.user.save()
        return redirect('home')
    else:
        return redirect('login')
