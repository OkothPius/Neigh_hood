from django.conf.urls import url 
from . import views 

urlpatterns = [
    url('',views.home, name='homePage'),
    url(r'^about/',views.home, name='AboutPage'),
]