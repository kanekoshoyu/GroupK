from django.http import HttpResponse
from .models import Picture, Tag
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
#forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    
    '''
    picture_set = Picture.objects.all()
    query = request.GET.get("q")
    if query:
        picture = picture_set.filter(
            title__icontains=query
        ).distinct()
        return render(request, 'index.html', {'pictures': picture,})
    else:
        return render(request, 'index.html', {'pictures': picture_set})
    
    '''
    query = request.GET.get("q")
    try:
        #1 Get the Tag Object
        requiredTag = Tag.objects.all().get(text=query)
        #2 Get the Photo Objects associated with the Tag
        requiredPicture = requiredTag.picture_set.all().distinct()
    except Tag.DoesNotExist:
        requiredTag = None
        requiredPicture = Picture.objects.all()
    return render(request, 'index.html', {'pictures': requiredPicture})
        


class DetailView(generic.DetailView):
    model = Picture
    template_name ='detail.html'


class PictureCreate(CreateView):
    model = Picture
    fields = ['title', 'description', 'category', 'file', 'uploader_name']
    #Create a Form for Tag
    #Add-to/Create Tags
    def form_valid(self, form):
        my_picture_uploader = form.instance.uploader_name
        pictures = Picture.objects.all()
        num = pictures.filter(uploader_name=my_picture_uploader).count()
        if num < 3:
            success = True
        else:
            success = False
        if success:
            return super(PictureCreate, self).form_valid(form)
        else:
            return HttpResponse("User Can't Upload too many Photos")


