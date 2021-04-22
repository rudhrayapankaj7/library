"""Library URL Configuration

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
from django.db.models.base import Model
from django.urls import path
from Book import views 
# sometimes it accepts from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),  # by default
    path('home/', views.homepage, name="welcome"),  # user defined url
    path('save-book/', views.save_book),
    path('edit-book/<int:id>/', views.edit_book),
    path('delete-book/<int:pk>/', views.delete_book),
    path('show-deleted-data/', views.show_deleted_data),
    path('h-delete-book/<int:pk>/', views.hard_delete_book),
    path('restore/<int:id>/', views.restore_book),
    path('home/all-restore-book/', views.all_restore_book),
    path('home/all-delete-book/', views.all_delete_book),


]





# http://127.0.0.1:8000/   # BASEURL
# http://127.0.0.1:8000/admin/   # Admin
