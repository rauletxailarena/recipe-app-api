from django.urls import path, include

from rest_framework.routers import DefaultRouter
from recipe import views

app_name = 'recipes'

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]