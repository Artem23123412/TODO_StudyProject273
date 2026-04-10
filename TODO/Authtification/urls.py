from django.urls import path
from . import views
urlpatterns = [
    path('', views.enter, name="enter"),
    path('authtificate/<string:mode>/', views.authtificate, name="auth"),
    path('reg/', views.register, name="reg"),
    path('login/', views.user_login, name="login"),
]