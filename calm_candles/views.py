from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def our_story(request):
    return render(request, 'our_story.html')

def our_blog(request):
    return render(request, 'our_blog.html')

def shop(request):
    return render(request, 'shop.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def shipping(request):
    return render(request, 'shipping.html')

def contact(request):
    if request.method == 'POST':
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Message from {name} ({email}): {message}")
    return render(request, 'contact.html')

from django.http import HttpResponse

def search(request):
    query = request.GET.get("q", "")
    return HttpResponse(f"Search results for: {query}")
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")