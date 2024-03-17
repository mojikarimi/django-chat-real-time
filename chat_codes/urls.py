"""
URL configuration for chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import re_path
from .views import *

urlpatterns = [
    # front
    re_path(r'^$', index, name='index'),
    re_path(r'^update_message$', update_message, name='update_message'),
    re_path(r'^add_message$', add_message, name='add_message'),
    # panel
    re_path(r'^panel_index$', panel_index, name='panel_index'),
    re_path(r'^panel_add_message$', panel_add_message, name='panel_add_message'),
    re_path(r'^panel_update_message$', panel_update_message, name='panel_update_message'),
]
