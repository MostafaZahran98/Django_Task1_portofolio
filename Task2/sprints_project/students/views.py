
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import MyForm
from .forms import MyForm1
def my_form(request):
  
  if request.method == "POST":
    form = MyForm(request.POST)
    
    if form.is_valid():
       form.save()
       return redirect('/form1')  
    
  else:
      form = MyForm()
      
  
  return render(request, 'show.html', {'form': form})

def my_form1(request):
  
  if request.method == "POST":
    form1 = MyForm1(request.POST)
    if form1.is_valid():
       form1.save()
       return redirect('/form')  
  else:
      form1 = MyForm1()
  return render(request, 'show1.html', {'form1': form1})
 

# Create your views here.
