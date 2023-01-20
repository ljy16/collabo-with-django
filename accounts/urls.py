from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # signup
    path('signup/', views.signup, name='signup'),
    
    # login
    # path('login/', views.login, name='login')
    
]
