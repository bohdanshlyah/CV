from django.urls import path

from resume.views import main

urlpatterns = [
    path('', main, name = 'main')
]
