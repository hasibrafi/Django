from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
#from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard', views.dashboardView, name="dashboard"),
    path('login/', views.LoginView.as_view(), name="login_url"),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', views.indexView, name="home"),

]