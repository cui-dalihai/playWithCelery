from django.db import models

# Create your models here.


class EndUser(models.Model):

    name = models.CharField(max_length=32, primary_key=True)
    age = models.CharField(max_length=32, blank=True, null=True)



