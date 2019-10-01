from django.conf.urls import url
from authapp import views

urlpatterns = [
    url('',views.index,name="index")
]