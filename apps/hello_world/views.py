from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
	text = "Hello"
	return HttpResponse(f'<!DOCTYPE html><html><body><h1>{text}, World!</h1></body></html>')
