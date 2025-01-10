from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PresentationViewSet
from .views import RegisterView

router = DefaultRouter()
router.register(r'presentations', PresentationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]