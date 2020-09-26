from rest_framework import viewsets, mixins
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer