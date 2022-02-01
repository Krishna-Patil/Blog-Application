from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', profile, name='update'),

]
