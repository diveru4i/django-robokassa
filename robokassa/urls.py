#coding: utf-8
from django.conf.urls import url

from robokassa.views import receive_result, success, fail


urlpatterns = [
    url(r'^result/$', receive_result, name='robokassa_result'),
    url(r'^success/$', success, name='robokassa_success'),
    url(r'^fail/$', fail, name='robokassa_fail'),
]
