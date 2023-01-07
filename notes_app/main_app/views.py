from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Notes App!')

def about(request):
  return render(request, 'about.html')

#Class View
class NoteList(ListView):
  model = Note
  template_name = 'notes/index.html'
  context_object_name = 'notes'

# Function based view for ALL cats
def notes_index(request):
  notes = Note.objects.all()
  return render(request, 'notes/index.html', { 'notes': notes })


class NoteCreate(CreateView):
  model = Note
  #fields = '__all__'
  # alternative method -> 
  fields = ['title', 'details']
  success_url = '/notes/'

def notes_detail(request, note_id):
  # get cat from DB based on the ID in URL
  note = Note.objects.get(id=note_id)
  # render some template
  return render(request, 'notes/detail.html', { 
    # include the cat and feeding_form in the context
    'note': note, 
    })

class NoteUpdate(UpdateView):
  model = Note
  fields = ['title', 'details']

class NoteDelete(DeleteView):
  model = Note
  success_url = '/notes/'