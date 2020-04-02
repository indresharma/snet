
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.AllGroupsView.as_view(), name='all_group'),
    path('<int:pk>/', views.GroupView.as_view(), name='main_group'),
    path('create_group/', views.GroupCreateView.as_view(), name='create_group'),
    path('update_group/<int:pk>/', views.GroupUpdateView.as_view(), name='update_group'),
    path('join_group/<int:id>/', views.join_group, name='join_group'),
    path('leave_group/<int:id>/', views.leave_group, name='leave_group'),
    path('<int:pk>/group_posts/', views.group_post, name='group_posts'),
    

    
    

]
