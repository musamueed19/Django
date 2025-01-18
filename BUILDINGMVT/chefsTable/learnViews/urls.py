from django.urls import path

from . import views

urlpatterns = [
    path('functional', views.learnHttpMethods),
    path('class',  views.MyView.as_view()),

]
