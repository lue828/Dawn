from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from dawn_app.models import Blog
from dawn_app.models import Author
from dawn_app.models import Tag

def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("blog_list.html", {"blogs": blogs})

def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"blog": blog})

def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_filter.html",
        {"blogs": blogs, "tag": tag, "tags": tags})