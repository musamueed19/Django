# import pth from django.urls
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('hello/', views.hello),
    path('menu/<int:menu_id>', views.menu_by_id, name="menu_by_id"),
    path('http/', views.learnHttpMethods),
]
