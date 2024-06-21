# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSetBook

router = DefaultRouter()
router.register(r'books', ViewSetBook)

urlpatterns = [
    path('', include(router.urls)),
]
