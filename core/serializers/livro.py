from attr import field, fields
from core.models import Livro
from rest_framework.serializers import ModelSerializer


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1