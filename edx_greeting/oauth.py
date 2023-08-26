from authlib.integrations.django_client import OAuth
from django.conf import settings

oauth = OAuth()
value = {
        # Set your own client_id and secret from the LMS here.
        'client_id': 'b3ACvjeT0Izcjaot2iGMeHgexQ1Rbud1vss47caV',
        'client_secret': 'XGPr5CNC2QiBTDtcZs2WFDdKsOz7PiMUY4J5SsOTq9IVrOt7hKYvnVuVgG0M3XQ37oDTGtvwDynnKbTH27ldLWZASpRePrRNrolaZVqSPbA2dIeiWzmCaLOZzpydygLX',
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

oauth.register('lms', value)
# for key, value in settings.AUTHLIB_OAUTH_CLIENTS.items():
#     # This will register the LMS as a client for Authlib.
#     # If you added any other providers to the AUTHLIB_OAUTH_CLIENTS
#     # settings dictionary, they'll be added, too.
#     oauth.register(key, **value)
