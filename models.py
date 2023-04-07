from django.db import models

# Create your models here.

class Registeration(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    contact_number = models.CharField("phone number",max_length=100)
    time = models.TimeField()
    subjects = models.IntegerField()

    def __str__(self):
        return self.name
