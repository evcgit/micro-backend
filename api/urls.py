from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProjectViewSet, DrawingViewSet, ComponentViewSet, UserViewSet

class NoTrailingSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trailing_slash = ''

router = NoTrailingSlashRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'drawings', DrawingViewSet)
router.register(r'components', ComponentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain token
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
] + router.urls
