from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .models import File
from rest_framework.response import Response
from rest_framework import status

from .tasks import process_file

from .serializers import FileSerializer, ListFileSerializer


class CreateFileViewSet(CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            file = serializer.save()
            process_file.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListFileViewSet(viewsets.GenericViewSet,
                      ListModelMixin):
    queryset = File.objects.all()
    serializer_class = ListFileSerializer
