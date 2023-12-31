from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('login', views.LoginView.as_view(), name='login'),
    path('detail', views.CustomUserDetailView.as_view(), name='user_detail'),
]
