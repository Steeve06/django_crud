from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    # path('login/', views.login_user, name='login'), uncommented this section if you want to create a separate login page
    path('logout/', views.logout_user, name='logout'),
]
