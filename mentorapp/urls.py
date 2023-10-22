from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.user_login_mentee, name="login"),
    path('login/', views.user_login_mentor, name="login"),
    path('signup_mentor/', views.mentor_signup, name="signup_mentor"),
    path('signup_mentee/', views.mentee_signup, name="signup_mentee"),
    path('logout/', views.user_logout, name="logout"),
]
