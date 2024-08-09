from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)
    prenom = models.CharField(max_length=31)
    salaire = models.IntegerField()
    date_adhesion=models.DateField(default=timezone.now)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}  {self.prenom}  "
  
class Presence(models.Model):
    id= models.AutoField(primary_key=True)
    personne=models.ForeignKey(Personne, on_delete=models.PROTECT, related_name="presence_personne")
    salaire = models.IntegerField()
    present= models.BooleanField()
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.personne }  {self.created_at.date()}"
    
class Salaire(models.Model):
    id=models.AutoField(primary_key=True)
    personne=models.ForeignKey(Personne, on_delete=models.PROTECT, related_name="salaire_personne")
    montant = models.IntegerField(editable=False)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personne }  {self.created_at.date()}" 
# Create your models here.
