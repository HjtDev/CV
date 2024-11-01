from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index_view(request):
    return render(request, 'index.html')
