from django.apps import AppConfig
from django.db.models.signals import pre_save


class LinkConfig(AppConfig):
    name = 'link'

    def ready(self):
        from link.models import Link
        pre_save.connect(Link.pre_save, Link)
