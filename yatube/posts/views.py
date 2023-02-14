from django.shortcuts import get_object_or_404, render

from .models import Group, Post

VIEW_COUNT_SELECTION = 10


def index(request):
    posts = Post.objects.select_related('group')[:VIEW_COUNT_SELECTION]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:VIEW_COUNT_SELECTION]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
