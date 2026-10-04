from attr import fields
from core.models import Livro
from rest_framework.serializers import ModelSerializer


class LivroSerializer(ModelSerializer):
    class meta:
        model: Livro
        fields = "__all__"
