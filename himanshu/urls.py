from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('signin/', views.sign_in, name="sign_in"),
    path('signup/', views.sign_up, name="sign_up"),

    # path('<str:operation>/<int:num1>/<int:num2>/', views.home),
    # path('name/fullname/', views.fullname)
]