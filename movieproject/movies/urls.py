from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('api/movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/movies/<int:id>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
