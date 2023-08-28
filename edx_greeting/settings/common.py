# coding=utf-8
"""
Common Pluggable Django App settings

Handling of environment variables, see: https://django-environ.readthedocs.io/en/latest/
to convert .env to yml see: https://django-environ.readthedocs.io/en/latest/tips.html#docker-style-file-based-variables
"""
from path import Path as path
import environ
import os

# path to this file.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

APP_ROOT = (
    path(__file__).abspath().dirname().dirname()
)  # /blah/blah/blah/.../example-digital-learning-openedx/openedx_plugin
REPO_ROOT = APP_ROOT.dirname()  # /blah/blah/blah/.../example-digital-learning-openedx


def plugin_settings(settings):
    """
    Injects local settings into django settings

    see: https://stackoverflow.com/questions/56129708/how-to-force-redirect-uri-to-use-https-with-python-social-app
    """

    # settings.SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
    # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    settings.CORS_ORIGIN_ALLOW_ALL = True

    settings.REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        ),
        # ...
    }

    settings.OAUTH2_PROVIDER = {
        'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,  # Set the token expiration time as needed
        'APPLICATION_MODEL': 'oauth2_provider.Application',  # Point to your Application model
    }

    settings.AUTHLIB_OAUTH_CLIENTS = {
        'lms': {
            # Set your own client_id and secret from the LMS here.
            'client_id': 'EbDVfkoZnQ8dm39v4N1VUDRRBQjNJtkp4A5nhW3w',
            'client_secret': 'B7vBK0kvSFQBfA7RBO6W8H5RDuCrkkvXpVioWmwutmQoSCzJw0V5fRT8uOlxKlRhzc6ucZvbh1IeO6XfE8MQSGHny6l0dXNDdjqKwZblooNsFf0QSQnJljzQhNguv8NE',
            # This is where your application will fetch access tokens from.
            'access_token_url': 'http://local.overhang.io/oauth2/access_token',
            'access_token_params': None,
            # This is where your application will redirect the user to
            # authenticate and authorize your application.
            'authorize_url': 'http://local.overhang.io/oauth2/authorize/',
            'authorize_params': None,
            # Authlib creates a client object that does a lot of the
            # heavy HTTP request work involved in the authentication
            # process for you.
            # You specify the root of the LMS API here. Since there are
            # a lot of different API paths in the LMS, we just pick
            # the root of the LMS as the URL.
            'api_base_url': 'http://local.overhang.io/',
            # The client can be given some additional customization.
            # For example, one thing we need to specify is the 'scopes'
            # our client will need access to. Here are a few of them.
            # The full list of available scopes can be found in the
            # edx-platform source-code, in lms/envs/common.py
            # within the OAUTH2_PROVIDER setting dictionary.
            'client_kwargs': {
                'scope': 'email profile read',
                'token_endpoint_auth_method': 'client_secret_basic',
                'token_placement': 'header',
            },
        }
    }

    settings.CORS_ORIGIN_ALLOW_ALL = True
    settings.CORS_ORIGIN_WHITELIST = (
        u'http://127.0.0.1:8000',
        u'http://local.overhang.io:8000',
        u'http://local.overhang.io:8000/greeting/'
    )
