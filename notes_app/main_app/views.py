from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

#Class View
#class NoteList(LoginRequiredMixin, ListView):
 # model = Note
  #template_name = 'notes/index.html'
  #context_object_name = 'notes'

# Function based view for ALL cats
@login_required
def notes_index(request):
  notes = Note.objects.filter(user=request.user)
  return render(request, 'notes/index.html', { 'notes': notes })

class NoteCreate(LoginRequiredMixin, CreateView):
  model = Note
  fields = ['title', 'details']
  #fields = '__all__'
  # alternative method -> 
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def notes_detail(request, note_id):
  # get cat from DB based on the ID in URL
  note = Note.objects.get(id=note_id)
  # render some template
  return render(request, 'notes/detail.html', { 
    # include the cat and feeding_form in the context
    'note': note, 
    })

class NoteUpdate(LoginRequiredMixin, UpdateView):
  model = Note
  fields = ['title', 'details']

class NoteDelete(LoginRequiredMixin, DeleteView):
  model = Note
  success_url = '/notes/'



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
