
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_post, name='delete'),
    path('<int:pk>/like/', views.like_post, name='like'),
    

]
