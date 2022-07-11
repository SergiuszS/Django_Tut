from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

class MainView(View):

    def get(self, request):
        context = {
            'page_title': 'First Django App'
        }
        return render(request, 'index.html', context)

def redirect(request):
    return HttpResponseRedirect('https://google.com')

def second_page(request):
    return render(request, 'second_page.html')        