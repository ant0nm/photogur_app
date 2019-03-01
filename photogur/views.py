from django.http import HttpResponse
from django.shortcuts import render
from photogur.models import Picture, Comment


def pictures_page(request):
    context = {'pics': Picture.objects.all()}
    html_string = render(request, 'pictures.html', context)
    return HttpResponse(html_string)
