"""
URL configuration for candle_business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.urls import path
from . import views  # Correctly importing views from the current app
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('our-story/', views.our_story, name='our_story'),
    path('our-blog/', views.our_blog, name='our_blog'),
    path('shop/', views.shop, name='shop'),
    path('shipping-information/', views.shipping, name='shipping'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('search/', views.search, name='search'),  # Ensure your search URL pattern is correctly added here  
]  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

