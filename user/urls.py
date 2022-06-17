from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.UserLoginLogout.as_view()),
    path('logout/', views.UserLoginLogout.as_view()),
    path('signup/', views.UserApiView.as_view())
]