from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=10000)
    time_modified = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):

        return self.title

    def get_absolute_url(self):
     return reverse('detail', kwargs={'note_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"
