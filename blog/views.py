from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello. You've reached our blog index")

def blogpost(request, post_id):
	return HttpResponse(Post.objects.get(post_id))
	
