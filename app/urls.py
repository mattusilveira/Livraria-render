from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from core.views import CategoriaViewSet, EditoraViewSet, UserViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()

router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'categorias', CategoriaViewSet, basename='categoria') 
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'editoras', EditoraViewSet, basename='editora')
router.register(r'livros', LivroViewSet, basename='livro')

urlpatterns = [
    path("api/media/", include(uploader_router.urls)),
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)