from rest_framework import authentication, permissions, viewsets

from .models import Sprint
from .serializers import SprintSerializer


class DefaultsMixin(object):
    """ Default settings for view authentication, permissions,
    filtering and pagination """

    authentication_classes = (
            authentication.BasicAuthentication,
            authentication.TokenAuthentication,
    )

    permission
class SprintViewSet(viewsets.ModelViewSet):
    """ API endpoint for listing and creating sprints. """

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
