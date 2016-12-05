from django.conf.urls import url, include
from . import views
from django.conf import settings

#from . import views

#urlpatterns =  ('',
#	url(r'^$', 'apps.inicio.views.index')
#)

urlpatterns =  [
	url(r'^$', views.index),
	url(r'^index/$', views.index2),
	url(r'^index2/$', views.index3),
#url(r'^index/$','apps.inicio.views.index'),
   #url(r'^$', 'apps.inicio.views.index'),
]