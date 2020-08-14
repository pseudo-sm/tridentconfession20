from django.db import models

# Create your models here.

class Confession(models.Model):

    datetime = models.DateTimeField(auto_now=True)
    confession = models.TextField()
    color = models.CharField(max_length=10)
    def __str__(self):
        return str(self.pk)