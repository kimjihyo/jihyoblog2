from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment, Tag
from django.utils import timezone

def index(request):
    context = {
        'all_posts': Post.objects.all().order_by('-pub_date')[:9],
        'all_tags': Tag.objects.all(),
    }
    return render(request, 'blog/main_page.html', context=context)

def detail(request, post_id):
    context = {
        'post': Post.objects.get(pk=post_id),
        'all_comments':  Comment.objects.filter(post=Post.objects.get(pk=post_id)).order_by('-pub_date'),
        'len_of_comments': len(Comment.objects.filter(post=Post.objects.get(pk=post_id))),
    }
    return render(request, 'blog/view_article.html', context=context)


def leave_comment(request, post_id):
    name = request.POST['comment-write-name']
    pw = request.POST['comment-write-pw']
    content = request.POST['content']

    if not (name and pw and content):
        return render(request, 'blog/view_article.html', context={
            'post': Post.objects.get(pk=post_id),
            'all_comments':  Comment.objects.filter(post=Post.objects.get(pk=post_id)).order_by('-pub_date'),
            'len_of_comments': len(Comment.objects.filter(post=Post.objects.get(pk=post_id))),
            'errormessage': 'Please fill in the blanks',
        })
    else:
        new_comment = Comment(name=name, pw=pw, content=content, post=Post.objects.get(pk=post_id))
        new_comment.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(post_id,)))

def view_archive(request):
    context = {
        'all_posts': Post.objects.all().order_by('-pub_date'),
        'all_tags': Tag.objects.all().order_by('name'),
    }
    return render(request, 'blog/archive.html', context=context)

def view_about(request):
    return render(request, 'blog/about.html', context={})

def view_admin(request):
    return render(request, 'blog/admin.html', context={})

def write_post(request):
    pass

def view_test(request):
    return render(request, 'blog/test.html', context={})