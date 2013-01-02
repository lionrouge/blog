# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from blog.models import Post#, Comment

def index(request):
	latest_posts_list = Post.objects.all().order_by('-pub_date')[:5]
	#req = request.body.decode('utf-8')
	#req = [str(x)+" : "+str(request.META.get(x)) for x in iter(request.META)]
	#req = request.readlines()
	#req = [str(x)+" : "+str(request.GET.dict().get(x)) for x in iter(request.GET.dict())]
	#req = []
	#for key in request.GET.iterkeys():
	#	valuelist = request.GET.getlist(key)
	#	req.extend(['%s=%s' % (key, val) for val in valuelist])
	#req.sort()
	#req = request.encoding
	return render_to_response(
	'posts/index.html',
		{'latest_posts_list' : latest_posts_list
		  #'req' : req
		}
	)
	
def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
		#comments = Comment.objects.filter(post__exact=p)
	except Post.DoesNotExist:
		raise Http404
	
	return render_to_response(
	'posts/detail.html',
	{	'post' : p
		#'comments' : comments
	}
	)