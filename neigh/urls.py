from django.conf.urls import url 
from . import views 

urlpatterns = [
    url('',views.home, name='homePage'),
    url(r'^signout/$',views.signout,name='signout'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^add_biz/',views.add_biz,name='add_biz'),
    url(r'^change_neighborhood/(\d+)',views.change_neighborhood,name='change_neighborhood'),
    url(r'^search/',views.search,name='search'),
]