from django.conf.urls import url, include
from .views import hire, make_estimate


urlpatterns = [
    url(r'^$', hire, name='hire'),
    url(r'^(?P<pk>\d+)/$', make_estimate, name='make_estimate'),
]
