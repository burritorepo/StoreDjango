from django.conf.urls import url
from .import views
from django.contrib.auth.views import login_required

app_name = 'shopcursos'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', login_required(views.product_list), name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
