from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SimpleHopeConstructionConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hope_construction'
    verbose_name = _("Hope Construction Ltd")


class HopeConstructionConfig(SimpleHopeConstructionConfig):
    """The default AppConfig for admin which does autodiscovery."""

    default = True

    def ready(self):
        super().ready()
