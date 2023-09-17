from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name="home"),
	path('registration', views.registration, name='registration'),
	path('login', views.login, name='login'),
	path('createevent', views.createevent, name='createevent'),
    path('wedding', views.wedding, name='wedding'),
    path('birthday', views.birthday, name='birthday'),
    path('concert', views.concert, name='concert'),
    path('corporate', views.corporate, name='corporate'),
    path('booking/<token>/', views.booking_function, name='booking'),
]