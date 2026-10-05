from core.models import Livro
from core.serializers import LivroSerializer, LivroRetrieveSerializer
from rest_framework.viewsets import ModelViewSet


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    
    def get_serializer_class(self):
        if self.action in {'list', 'retrieve'}:
            return LivroRetrieveSerializer
        return LivroSerializer
