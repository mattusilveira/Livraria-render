from rest_framework.serializers import ModelSerializer
from core.serializers import (
    LivroRetrieveSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
from core.models import Livro

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco")

class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1