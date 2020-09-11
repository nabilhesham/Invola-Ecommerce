from django.conf import settings
from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter

from products.api.views import coffee_machine_data, coffee_pod_data


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


coffee_machine_url = [url("coffee_machine_data", coffee_machine_data, name="coffee_machine_data")]
coffee_pod_url = [url("coffee_pod_data", coffee_pod_data, name="coffee_pod_data")]

app_name = "api"
urlpatterns = (
    router.urls + coffee_machine_url + coffee_pod_url
)
