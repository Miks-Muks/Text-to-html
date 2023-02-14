from django.shortcuts import render
from .forms import EditorForm


# Create your views here.
def convector(request):
    form = EditorForm()
    return render(request, 'index.html',context={'form':form})
