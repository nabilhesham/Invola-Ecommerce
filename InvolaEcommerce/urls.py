from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    # API base url
    path("api/", include("InvolaEcommerce.api_router"))
]
