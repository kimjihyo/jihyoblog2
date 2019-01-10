from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.view_archive, name='index'),
    path('archive/', views.view_archive, name='archive'),
    path('about/', views.view_about, name='about'),
    path('view_admin/', views.view_admin, name='view_admin'),
    path('test/', views.view_test, name='test'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]