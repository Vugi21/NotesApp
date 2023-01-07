from django.db import models

# Create your models here.
class notes(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=10000)
    time_modified = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        
        return self.title
