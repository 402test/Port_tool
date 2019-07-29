# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2019/7/29 14:35'

from django.urls import path
from django.conf.urls import url
from index.views import Index_View
urlpatterns = [
    url('',Index_View.as_view()),
]