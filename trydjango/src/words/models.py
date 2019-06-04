from django.db import models

# Create your models here.
class Word(models.Model):
    word        = models.CharField(max_length=100)
    definition  = models.TextField(null=True, blank=True, default="Description")
    examples    = models.TextField(null=True, blank=True, default="Examples")