"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

admin.site.site_header = 'Recipe Sharing App'
admin.site.site_title = 'Recipe Sharing'
admin.site.index_title = 'Welcome to Recipe Sharing'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('register/', user_views.register, name="user-register"),
    # new urls
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
    path('profile/', user_views.profile, name="user-profile"),
]
