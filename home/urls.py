from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name="home"),
	path('registration', views.registration, name='registration'),
	path('login', views.login, name='login'),
	path('createevent', views.createevent, name='createevent'),
    path('events', views.eventshow, name='events'),
    path('contacts', views.contacts, name='contacts'),
    path('birthday', views.birthday, name='birthday'),
    path('booking', views.booking, name='booking'),
]