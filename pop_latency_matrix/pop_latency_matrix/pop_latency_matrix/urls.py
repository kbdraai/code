"""
Definition of urls for pop_latency_matrix.
"""

from django.conf.urls import url
import django.contrib.auth.views
import app.views

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
]
