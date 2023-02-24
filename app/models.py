from django.db import models

# Create your models here.

class Confession(models.Model):

    datetime = models.DateTimeField(auto_now=True)
    confession = models.TextField()
    color = models.CharField(max_length=10)
    site = models.CharField(max_length=200)
    
    def __str__(self):
        if len(self.confession[:30]) < 30:
            return self.confession[:30]  
        else:
            return self.confession[:30]+'...'

    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'

    

class Site(models.Model):
    site = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
    
    def __str__(self):
        return self.site