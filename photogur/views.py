from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment


def pictures_page(request):
    context = {'pics': Picture.objects.all()}
    html_string = render(request, 'pictures.html', context)
    return HttpResponse(html_string)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    html_string = render(request, 'picture.html', context)
    return HttpResponse(html_string)

def picture_search(request):
    # request.GET is a dictionary where keys are form filed names (that we assigned) and values are data entered by the user
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}
    html_string = render(request, 'search.html', context)
    return HttpResponse(html_string)

def create_comment(request):
    post_dict = request.POST
    picture = Picture.objects.get(pk=post_dict['picture'])
    name = post_dict['comment-name']
    message = post_dict['comment-message']
    new_comment = Comment.objects.create(name=name, message=message, picture=picture)
    path = '/pictures/' + str(picture.pk)
    return HttpResponseRedirect(path)
