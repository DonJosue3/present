from django.urls import path,include
from urusoro.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView   

router = DefaultRouter()
router.register("personnes",PersonneViewSet, basename="personne")
router.register("presences",PresenceViewSet, basename="presence")
router.register("salaire",SalaireViewSet, basename="salaire")

urlpatterns=[
    path("",include(router.urls)),
    path("api_login", include("rest_framework.urls")),
    path("login",TokenObtainPairView.as_view()),
]
       