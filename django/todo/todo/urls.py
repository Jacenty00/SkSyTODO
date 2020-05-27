"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from tasks.views import add_view , impressum_view , edit_view , home_view, add_todo, del_todo ,edit_todo,edit_del_todo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('add/', add_view, name='add'),
    path('edit/', edit_view, name='edit'),
    path('edit.html', edit_view, name='edit'),
    path('impressum/', impressum_view, name='impressum'),
    path('add_todo/', add_todo, name='add_todo'),
    path('edit_todo/', edit_todo, name='edit_todo'),
    path('del_todo/', del_todo, name='del_todo'),
    path('edit_del_todo/', edit_del_todo, name='edit_del_todo')
]
