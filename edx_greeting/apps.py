"""
edx_greeting Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs


class EdxGreetingConfig(AppConfig):
    """
    Configuration for the edx_greeting Django application.
    """

    name = 'edx_greeting'
    label = 'edx_greeting'

    plugin_app = {
        PluginURLs.CONFIG: {
            'lms.djangoapp': {
                PluginURLs.NAMESPACE: name,
                PluginURLs.APP_NAME: name,
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        PluginSettings.CONFIG: {
            'lms.djangoapp': {
                'production': {
                    PluginSettings.RELATIVE_PATH: "settings.production"
                },
                'common': {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            }
        },
    }
