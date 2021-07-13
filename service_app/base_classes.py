from rest_framework import viewsets


class BaseView(viewsets.mixins.ListModelMixin,
               viewsets.mixins.RetrieveModelMixin,
               viewsets.mixins.CreateModelMixin,
               viewsets.mixins.UpdateModelMixin,
               viewsets.mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    queryset = None
    serializer_class = None
