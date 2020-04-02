from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', user_views.ProfileView.as_view(), name='profile'),
    path('register/', user_views.Register.as_view(), name='register_profile'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('update_profile/<int:pk>/', user_views.UpdateProfile.as_view(), name='update_profile'),
    
]