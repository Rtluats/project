from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Project",
        default_version="v1",
        description="Empty",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger = path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')