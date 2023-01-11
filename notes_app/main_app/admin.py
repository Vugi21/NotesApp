from django.contrib import admin

# Register your models here.
from .models import Note, Photo

admin.site.register(Note)
admin.site.register(Photo)