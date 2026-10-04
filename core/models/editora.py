from django.db import models

from django.forms.fields import CharField

from django.template.defaultfilters import length

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nome
    