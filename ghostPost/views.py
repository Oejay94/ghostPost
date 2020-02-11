from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from ghostPost.models import BoastRoast
from ghostPost.forms import PostForm


def home(request):
    data = BoastRoast.objects.all().order_by("-time")
    return render(request, 'home.html', {'data': data})


def upvote(request, id):
    try:
        post = BoastRoast.objects.get(id=id)
    except BoastRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('home'))
    post.total += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def downvote(request, id):
    try:
        post = BoastRoast.objects.get(id=id)
    except BoastRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('home'))
    post.total -= 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


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
    data = BoastRoast.objects.filter(boast_or_roast=True).order_by('-time')
    return render(request, html, {'data': data})


def roast_view(request):
    html = 'home.html'
    data = BoastRoast.objects.filter(boast_or_roast=False).order_by('-time')
    return render(request, html, {'data': data})
