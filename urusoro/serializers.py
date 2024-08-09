from rest_framework import serializers
from .models import *

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personne
        fields="__all__"

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Presence
        fields="__all__" 
class SalaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Salaire
        fields="__all__"   

    def to_representation(self, instance):
        data=super().to_representation(instance)
        data["created_by"]=instance.created_by.username
        data["ikindi kintu"]="amanyanga"
        data["personne"]=PersonneSerializer(instance.personne).data
        return data  