from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import BasePermission
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
class IsAuthenticatedForReadOrIsAdmin(BasePermission):
    def has_permission(self,request,view):
        user=request.user
        if user.is_authenticated: 
            if request.method in ["GET","PUT","PATCH"]:
                return True
        if user.is_superuser:
            return True
        return False    
class PresenceViewSet(viewsets.ModelViewSet):
    queryset=Presence.objects.all()
    serializer_class=PresenceSerializer
    permission_classes=IsAuthenticatedForReadOrIsAdmin,
    authentication_classes=JWTAuthentication , SessionAuthentication
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)
class PersonneViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset= Personne.objects.all()
    serializer_class=PersonneSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields={
        "id":["exact"], 
    }
    search_fields=["prenom","nom"]
class SalaireViewSet(viewsets.ModelViewSet):
    queryset=Salaire.objects.all()
    serializer_class=SalaireSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields={
        "id":["exact"]
    }
    def perform_create(self,serializer):
        data=serializer.validated_data
        personne=data["personne"]
        presenses=Presence.objects.filter(personne=personne, present=True).count()
        montant=presenses*personne.salaire
        serializer.save(created_by=self.request.user ,montant= montant)


# Create your views here.
