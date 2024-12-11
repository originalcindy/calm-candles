from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'our_story.html')

def about(request):
    return render(request, 'our_blog.html')

def about(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'contact_us.html')

def about(request):
    return render(request, 'shipping.html')

def contact(request):
    if request.method == 'POST':
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Message from {name} ({email}): {message}")
    return render(request, 'contact.html')
