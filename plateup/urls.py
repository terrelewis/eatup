from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from plateup import views

urlpatterns = [
    url(r'^restaurants/$', views.RestaurantList.as_view()),
    url(r'^restaurants/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),

    url(r'^users/$' ,views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)