"""flight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('contact/', views.contact, name='contact'),
    path('login/', views.login_main, name='login'),
    path('logout/', views.logout, name='logout'),
    path('loading/', views.loading, name='loading'),
    path('flight-index-1/', include('flights.urls')),
    path('flight-index-1/result', include('search.urls'))
    #path('register/', views.register_page, name='register'),
    #path('products/', include(('products.urls', 'products'), namespace='products')),
    #path('search/', include(('search.urls', 'search'), namespace='search')),
]
if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
