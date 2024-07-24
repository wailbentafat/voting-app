from django.urls import path
from . import views

urlpatterns = [
    path('usercreate', views.create_user, name='create_user'),
    path('login', views.signup, name='login'),
    path('enter_profile/<int:user_id>', views.enter_profile, name='enter_profile'),
]