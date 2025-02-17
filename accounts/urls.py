"""URLS for Accounts"""


from django.urls import path, include

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register')
]