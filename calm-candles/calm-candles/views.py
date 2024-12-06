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
