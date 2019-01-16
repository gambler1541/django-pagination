from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from .models import Constacts


def listing(request):
    contact = Constacts.objects.all()
    p = Paginator(contact, 5)
    page = request.GET.get('page')

    try:
        posts = p.page(page)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)

    return render(request, 'list.html', {'posts' : posts})
