from django.shortcuts import render

# Create your views here.
from .models import details

def home(request):
    return render(request, 'bank/index.html')

def Details(request):
    detail = details.objects.all()
    context = {'detail':detail}
    return render(request, 'bank/details.html', context)