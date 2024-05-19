from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
