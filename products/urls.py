from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
url(r'^$', views.product_list, name='product_list'),
path('search/', views.search, name='Search'),
url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
