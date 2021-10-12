from django.urls import path,include
from .views import login,signup,social_login,social_signup
urlpatterns = [
    path('login/',login.as_view(),name='Login'),
    path('signup/',signup.as_view(),name='Signup'),
    path('login/social/',social_login.as_view(),name='Login'),
    path('signup/social/',social_signup.as_view(),name='Signup'),

]
