from django.urls import path
from .views import *


app_name = 'business'

urlpatterns = [
    path('',HomePage.as_view(), name='homepage'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('create_plan/', CreateBusinessPlan.as_view(), name='create'),
    
]
