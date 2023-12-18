from django.db import models

# Create your models here.
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=20)



class JobListing(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)


    
