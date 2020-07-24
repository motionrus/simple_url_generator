from django.db import models
import random
from simple_url_generator.settings import SITE_URL

KEY_LENGTH = 10


def _generate_key():
    key = ''
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    key_length = KEY_LENGTH
    for y in range(key_length):
        key += char[random.randint(0, len(char) - 1)]
    return key


class Link(models.Model):
    link_key = models.CharField(verbose_name='short link key', max_length=KEY_LENGTH, unique=True, )
    long_link = models.URLField(verbose_name='ling link', )

    @property
    def short_link(self):
        return SITE_URL + self.link_key

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        instance.link_key = _generate_key()

    class Meta:
        verbose_name_plural = "Links"
        verbose_name = "Link"
