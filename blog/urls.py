from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list_what_is_this_for'),
]
