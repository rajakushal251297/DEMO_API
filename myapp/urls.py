from django.contrib import admin
from django.urls import path,include
from .views import ProductViewSet 
from rest_framework import routers
from rest_framework.authtoken import views
router=routers.DefaultRouter()
router.register(r"product",ProductViewSet)

urlpatterns = [
    path("api-token-auth/",views.obtain_auth_token),
    path("",include(router.urls))

]



# python manage.py seed myapp --number=20