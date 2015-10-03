from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='blog'),
	url(r'^index/', views.index, name='index'),
	url(r'^(?P<post_id>[0-9]+)/$', views.blogpost, name='blogpost'),
	]
