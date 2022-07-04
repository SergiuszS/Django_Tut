from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'page_title': 'First Django App'
    }
    return render(request, 'index.html', context)

def second_page(request):
    return render(request, 'second_page.html')