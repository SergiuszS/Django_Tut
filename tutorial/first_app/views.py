from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'page_title': 'First Django App'
    }
    return render(request, 'index.html', context)