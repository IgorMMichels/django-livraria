from django.db import models

class Autor(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=18) # (555) 98409-4842
    def __str__(self):
        return self.nome