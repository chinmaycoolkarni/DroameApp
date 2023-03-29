"""droame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('forgot-password/', views.forgotPassword, name='forgot-pass'),
    path('logout/', views.logout, name='logout'),
    path('customers/', views.customers, name='customers'),
    path('addCustomer/', views.addCustomer, name='add-customer'),
    path('editCustomer/<int:customer_id>', views.editCustomer, name='edit-customer'),
    path('removeCustomer/<int:customer_id>', views.removeCustomer, name='remove-customer'),
    path('droneshots/', views.droneshots, name='droneshots'),
    path('addDroneShot/', views.addDroneShot, name='add-drone-shot'),
    path('editDroneShot/<int:drone_shot_id>', views.editDroneShot, name='edit-drone-shot'),
    path('removeDroneShot/<int:drone_shot_id>', views.removeDroneShot, name='remove-drone-shot'),
]
