from django.db import models

class User(models.Model):
    """
        simple user class
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


