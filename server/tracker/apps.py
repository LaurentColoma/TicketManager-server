"""
Application configuration file.

see https://docs.djangoproject.com/fr/1.9/ref/applications/.
"""

from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _
from importlib import import_module


class TrackerConfig(AppConfig):
    """
    Application configuration class.

    TODO
    """

    name = "tracker"
    verbose_name = _("Tracker")

    def ready(self):
        import_module("{}.signals".format(self.name))
