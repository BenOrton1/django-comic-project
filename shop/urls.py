from django.conf.urls import url, include
from .views import shop

urlpatterns = [
    url(r'^$', shop, name='shop'),
]