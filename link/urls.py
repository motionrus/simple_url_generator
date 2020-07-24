from django.urls import include, path
from rest_framework import routers

from link.viewsets import LinkViewSet, redirect_view_link

router = routers.DefaultRouter()
router.register(r'', LinkViewSet)

urlpatterns = [
    path(r'link/', include(router.urls)),
    path('<slug:url>/', redirect_view_link, name='redirect_view_link'),
]
