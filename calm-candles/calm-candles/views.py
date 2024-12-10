from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def our_story(request):
    return render(request, 'main/our_story.html')

def our_blog(request):
    return render(request, 'main/our_blog.html')

def shop(request):
    return render(request, 'main/shop.html')

def shipping(request):
    return render(request, 'main/shipping.html')

def contact_us(request):
    return render(request, 'main/contact_us.html')

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
