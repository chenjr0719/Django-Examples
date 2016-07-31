from django.shortcuts import render

# Create your views here.

def examples_index(request):
    return render(request, 'index.html')
