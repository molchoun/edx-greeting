import logging

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_provider.views.generic import ProtectedResourceView
from edx_greeting.oauth import oauth
from edx_greeting.serializers import GreetingSerializer

logger = logging.getLogger(__name__)


def login(request):
    # build a full authorize callback uri
    redirect_uri = request.build_absolute_uri('/authorize/')
    print(redirect_uri)
    return oauth.lms.authorize_redirect(request, redirect_uri)

@csrf_protect
def authorize(request):
    # This will create a http request client that points to the LMS.
    lms = oauth.create_client('lms')
    # Here, we authenticate the client with the token we got from the LMS. In a real-world
    # application, we'd save this token somehow for subsequent requests.
    username = request.user.username

    token = lms.authorize_access_token(request)
    # And then, we use this token to fetch the user's info.
    response = lms.get(f'/api/user/v1/accounts/{username}', token=token)
    response.raise_for_status()
    profile = response.json()
    msg = ""
    if request.method == "POST":
        msg = request.POST["msg"]
        if msg.lower() == "hello":
            msg = "goodbye"


    logger.info("Greeting")
    # Now that we have the user's info, we can render a page with the relevant info.
    return render(request, 'authorize.html', {'profile': profile, 'msg': msg})


class GreetingView(ProtectedResourceView):
    def perform_recursive_call(self, request, state):
        redirect_uri = request.build_absolute_uri('/greeting')
        oauth.lms.authorize_redirect(request, redirect_uri, state=state)

    def post(self, request):
        logger.info(f"\n{'='*30}aasgasg!!!!!!!!!!!!!!!!")
        state = request.POST.get('state')
        redirect_uri = request.build_absolute_uri('/greeting')
        logger.info(f"\n{'=' * 20}\nredirect_url: {redirect_uri}")
        oauth.lms.authorize_redirect(request, redirect_uri)
        lms = oauth.create_client('lms')
        logger.info(f"\n{'=' * 20}\nauthorized")
        username = request.user.username
        logger.info(f"\n{'='*20 }\n user: {username}")

        logger.info(f"\n{'=' * 20}\nstate: {state}")

        token = lms.authorize_access_token(request)
        logger.info(f"\n{'='*20 }\ntoken: {token}")
        response = lms.get(f'/api/user/v1/accounts/{username}', token=token)
        response.raise_for_status()

        serializer = GreetingSerializer(data=request.data)

        if serializer.is_valid():
            message = serializer.data["text"]

            if message == "hello":
                message = "goodbye"
                request.data["text"] = message
                self.post(request)
                return Response({"user": username, "text": message})

        message = request.data["text"]
        return Response({"user": "username", "text": message})


