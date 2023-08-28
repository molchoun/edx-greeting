"""
URLs for edx_greeting.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from django.urls import path, include
from edx_greeting import views
from django.views.decorators.csrf import csrf_exempt
import oauth2_provider.views as oauth2_views


oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]


urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="edx_greeting/base.html")),
    path('', views.login, name='index'),
    path('authorize/', views.authorize),
    path('api/greeting/', csrf_exempt(views.GreetingView.as_view())),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
]


# {
# "text": "hello"
# }

# e7zeykKqNPeXHiJAE4f39WfCgLMJj8Hi3PgCif82
# tpDjZ2XBtUA3y8HQqYkqJ7sBtvGGr624SlA5kLgztebxvbVUWK9zw996NDE3f91i8PUbKdGySui8UDBQWQsUIwDxiszRGqMPaG17iahYmjIE3tEmtLaHwFnc2he1AIyV
