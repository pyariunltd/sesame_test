
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post', views.new_post, name='new_post')
]