"""
URLs for edx_greeting.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from django.urls import path
from edx_greeting import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="edx_greeting/base.html")),
    path('', views.login, name='index'),
    path('authorize/', views.authorize),
    path('greeting/', csrf_exempt(views.GreetingView.as_view()))
]
