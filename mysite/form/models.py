from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=250)
    goal = models.CharField(max_length=250)

    def __str__(self):
        return self.name