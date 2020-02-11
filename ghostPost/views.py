from django.shortcuts import render, HttpResponseRedirect, reverse

from ghostPost.models import BoastRoast
from ghostPost.forms import PostForm


def home(request):
    data = BoastRoast.objects.all().order_by("-time")
    return render(request, 'home.html', {'data': data})


def postDetail(request, id):
    html = 'postDetail.html'
    data = BoastRoast.objects.get(id=id)
    return render(request, html, {'data': data})


def upvote(request, id):
    post = BoastRoast.objects.get(id=id)
    post.total += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, id):
    post = BoastRoast.objects.get(id=id)
    post.total -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addPost(request):
    html = 'addpost.html'

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastRoast.objects.create(
                title=data['title'],
                content=data['content'],
                boast_or_roast=data['boast_or_roast']
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm()

    return render(request, html, {'form': form})


def boast_view(request):
    html = 'home.html'
    data = BoastRoast.objects.filter(boast_or_roast=1).order_by('-time')
    return render(request, html, {'data': data})


def roast_view(request):
    html = 'home.html'
    data = BoastRoast.objects.filter(boast_or_roast=0).order_by('-time')
    return render(request, html, {'data': data})


def sort_by_votes(request):
    html = "home.html"
    data = BoastRoast.objects.all().order_by("-total")
    return render(request, html, {'data': data})
