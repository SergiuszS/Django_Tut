from django.shortcuts import render
from django.views import View

# Create your views here.

class MainView(View):

    def get(self, request, foo):
        context = {
            'page_title': 'First Django App',
            'foo': foo
        }
        return render(request, 'index.html', context)