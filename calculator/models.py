from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=40, blank=True, null=True)