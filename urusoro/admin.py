from typing import Any
from django.contrib import admin
from .models import *
@admin.register(Personne)
class personneAdmin(admin.ModelAdmin):
    list_display="nom", "prenom", "salaire", "created_by", "created_at", "date_adhesion"
    actions=["marquer_comme_present","doubler"]
    def save_model(self, request, obj, form, change) :
        obj.created_by=request.user
        obj.save()
    def marquer_comme_present(self, request, personnes)  :  
        for umuntu in personnes:
            Presence(personne = umuntu, salaire= umuntu.salaire,present = True, created_by=request.user).save()
    marquer_comme_present.short_description = "marquer ces gens comme present aujourd'hui "
    def doubler(self,request,personnes):
       for personne in personnes :
           personne.salaire= personne.salaire*2
           personne.save()
    doubler.short_description="doubler le salaire"    
@admin.register(Presence)   
class presenceAdmin(admin.ModelAdmin) :
    list_display="personne", "salaire","present", "created_by", "created_at",
    actions=["inverser"]
    def save_model(self, request, obj, form, change) :
        obj.created_by=request.user
        obj.save()
    def inverser(self,request,personnes)    :
        for umuntu in personnes:
              umuntu.present=not umuntu.present   
              umuntu.save()
    inverser.short_description="inverser"  
@admin.register(Salaire)
class salaireAdmin(admin.ModelAdmin):
    list_display="personne", "montant", "created_by", "created_at",
    def save_model(self, request, obj, form, change) :
        personne=obj.personne
        nb_presence=Presence.objects.filter(personne =personne).count()
        obj.montant=nb_presence*personne.salaire
        obj.created_by=request.user
        obj.save()
# Register your models here.
 

