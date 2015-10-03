from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from blog.models import Post, PostContent

def main(request):
	blog_post_list = Post.objects.order_by('-pub_date')[:5]	
	return render(request, 'blog/main.html', {'blog_post_list': blog_post_list})
	
	
def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	template = loader.get_template('blog/index.html')
	context = RequestContext(request, {'latest_post_list': latest_post_list,})
	return HttpResponse(template.render(context))
	
def blogpost(request, post_id):
	try:
		post=Post.objects.get(id=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	try:
		active_id= post.active_revision_id
		content=post.postcontent_set.get(revision_number=active_id)	
	except PostContent.DoesNotExist:
		raise Http404("Post Content does not exist")
	return render(request, 'blog/blogpost.html', {'post': post, 'content':content})
