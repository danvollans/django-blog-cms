from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from Homemade.forms import *
from Homemade.models import *
from django.core.exceptions import ObjectDoesNotExist
from django import forms


def current_pages():
    SidebarPages = [dict(short_name='home', display_name='Home', view='/home/', dynamic=False),
                    dict(short_name='posts', display_name='Blog', view='/posts/', dynamic=False)]

    for possible_page in Pages.objects.all():
        SidebarPages.append(dict(short_name=possible_page.page_name.lower().replace(" ", "-"),
                                 display_name=possible_page.page_name,
                                 view='/view_page/%s' % possible_page.id,
                                 dynamic=True,
                                 page_id=possible_page.id))

    SidebarPages.append(dict(short_name='admin', display_name='Admin', view='/admin/', dynamic=False))

    return SidebarPages

def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = AddPost()

    return render(request, 'add_post.html', {
        'current_view': 'add_post',
        'sidebar_pages': current_pages(),
        'form': form
    })


def add_tags(request):
    if request.method == 'POST':
        form = AddTags(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = AddTags()

    return render(request, 'add_post.html', {
        'current_view': 'add_tags',
        'sidebar_pages': current_pages(),
        'form': form
    })


def posts(request, post_id=False):
    if not post_id:
        selected_posts = Posts.objects.all().order_by("-id")
    else:
        selected_posts = Posts.objects.get(id=post_id)
        selected_posts = [selected_posts]

    return render(request, 'posts.html', {
        'current_view': 'posts',
        'sidebar_pages': current_pages(),
        'posts': selected_posts
    })


def home(request):
    # Get the latest post from the database
    latest_post = Posts.objects.all().order_by("-id")[0]
    posts = [latest_post]

    return render(request, 'home.html', {
        'current_view': 'home',
        'sidebar_pages': current_pages(),
        'posts': posts
    })


def edit_page(request, page_id=False):
    if request.method == 'POST':
        if page_id:
            form = AddPage(request.POST, instance=Pages.objects.get(pk=page_id))
        else:
            form = AddPage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    elif page_id:
        page = Pages.objects.get(pk=page_id)
        form = AddPage(instance=page)
    else:
        form = AddPage()

    return render(request, 'edit_page.html', {
        'current_view': 'edit_page',
        'sidebar_pages': current_pages(),
        'form': form
    })


def view_page(request, page_id):
    try:
        page = Pages.objects.get(pk=page_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/home/')

    return render(request, 'view_page.html', {
        'current_view': page.page_name.lower().replace(" ", "-"),
        'sidebar_pages': current_pages(),
        'page_name': page.page_name,
        'page_html': page.page_html
    })