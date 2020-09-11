from rest_framework import permissions, status, serializers, viewsets

from rest_framework.decorators import (
    action,
    api_view,
    permission_classes,
    renderer_classes,
)

from rest_framework.renderers import (
    JSONRenderer,
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
    StaticHTMLRenderer,
)
from rest_framework.request import Request
from rest_framework.response import Response

from json import dumps, loads
from products.models import CoffeePod, CoffeeMachine


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def coffee_machine_data(request: Request):
    result = {}
    try:
        qs = CoffeeMachine.objects.all().values()

        result["coffee_machines"] = qs
        return Response(status=status.HTTP_200_OK, data=result)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error in coffee machines": f"{e}"})\


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def coffee_pod_data(request: Request):
    result = {}
    try:
        qs = CoffeePod.objects.all().values()

        result["coffee_pods"] = qs
        return Response(status=status.HTTP_200_OK, data=result)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error in coffee machines": f"{e}"})


