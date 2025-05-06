from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Handle any custom logic if needed, then save the instance
        return super().update(request, *args, **kwargs)
