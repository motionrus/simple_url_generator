from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponseRedirect, JsonResponse, Http404
from link.models import Link
from django.db import models
from link.serializer import LinkSerializer
from rest_framework import mixins


class LinkViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


def redirect_view_link(request, url):
    try:
        link = Link.objects.get(link_key=url)
    except models.ObjectDoesNotExist:
        raise Http404("link does not exist")
    return HttpResponseRedirect(link.long_link)
