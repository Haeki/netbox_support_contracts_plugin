from django.db import models


class SupportContract(models.Model):
    """
    A database table representing animals and the sound each makes.
    """
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

