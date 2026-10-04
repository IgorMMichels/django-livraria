from rest_framework.viewsets import ModelViewSet

from core.models import Editora, editora
from core.serializers import EditoraSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all();
    serializer_class = EditoraSerializer