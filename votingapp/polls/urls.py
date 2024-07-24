from django.urls import path
from . import views

urlpatterns = [
    path('usercreate', views.create_user, name='create_user'),
    path('login', views.signup, name='login'),
    path('enter_profile/<int:user_id>', views.enter_profile, name='enter_profile'),
    path('get_events', views.get_events, name='get_events'),
    path('get_candidates/<int:event_id>', views.get_candidates, name='get_candidates'),
    path('vote/<int:event_id>/<int:candidate_id>', views.vote, name='vote'),
]