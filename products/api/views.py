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
# @permission_classes([permissions.IsAuthenticated])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def coffee_machine_data(request: Request):
    result = {}
    try:
        qs = CoffeeMachine.objects.all().values()

        # product type filter
        product_type = request.query_params.get("product_type", "")
        if product_type:
            qs = qs.filter(product_type=product_type)

        # water line filter
        water_line = request.query_params.get("water_line", "")
        if water_line == "true":
            qs = qs.filter(water_line_compatible=True)
        elif water_line == "false":
            qs = qs.filter(water_line_compatible=False)

        result["coffee_machines"] = qs
        return Response(status=status.HTTP_200_OK, data=result)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error in coffee machines": f"{e}"})\



@api_view(["GET"])
# @permission_classes([permissions.IsAuthenticated])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def coffee_pod_data(request: Request):
    result = {}
    try:
        qs = CoffeePod.objects.all().values()

        # product type filter
        product_type = request.query_params.get("product_type", "")
        if product_type:
            qs = qs.filter(product_type=product_type)

        # coffee flavor filter
        coffee_flavor = request.query_params.get("coffee_flavor", "")
        if coffee_flavor:
            qs = qs.filter(coffee_flavor=coffee_flavor)

        # pack size filter
        pack_size = request.query_params.get("pack_size", "")
        if pack_size:
            qs = qs.filter(pack_size=pack_size)

        result["coffee_pods"] = qs
        return Response(status=status.HTTP_200_OK, data=result)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error in coffee machines": f"{e}"})


