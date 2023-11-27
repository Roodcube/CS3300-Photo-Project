from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):


# Render the HTML template index.html with the data  in the
# content variable.
    photographer_active_galleries = Photographer.objects.select_related('gallery').all()
    print("active gallery query set", photographer_active_galleries)
    return render( request, 'photo_app/index.html', {'photographer_active_galleries':photographer_active_galleries})

class PhotographerListView(generic.ListView):
    model = Photographer
class PhotographerDetailView(generic.DetailView):
    model = Photographer
class GalleryDetailView(generic.DetailView):
    model = Gallery
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.filter(gallery=self.object)
        return context
        
class PhotoListView(generic.ListView):
    model = Photo
class PhotoDetailView(generic.DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Photo, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked
        return context

def photoLike(request, pk):
    photo = get_object_or_404(Photo, id=request.POST.get('photo_id'))

    if photo.likes.filter(id=request.user.id).exists():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)

    return HttpResponseRedirect(reverse('photo-detail', args=[str(pk)]))


def createPhoto(request, gallery_id):
    form = PhotoForm()
    gallery = Gallery.objects.get(pk=gallery_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and gallery_id
        photo_data = request.POST.copy()
        photo_data['gallery_id'] = gallery_id
        
        form = PhotoForm(photo_data, request.FILES)
        if form.is_valid():
            # Save the form without committing to the database
            photo = form.save(commit=False)
            # Set the portfolio relationship
            photo.gallery = gallery
            photo.save()

            # Redirect back to the gallery detail page
            return redirect('gallery-detail', gallery_id)

    context = {'form': form}
    return render(request, 'photo_app/photo_form.html', context)

def deletePhoto(request, gallery_id, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    
    if request.method == 'POST':
        photo_data = Photo.objects.get(pk=photo_id)
        photo_data.delete()

        # Redirect back to the gallery detail page
        return redirect('gallery-detail', gallery_id)
    
    context = {'ITEM': photo}
    return render(request, 'photo_app/delete_photo.html', context)

def editPhoto(request, gallery_id, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    form = PhotoForm(instance=photo)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)

    if form.is_valid():
        form.save()
        return redirect('gallery-detail', gallery_id)
    
    context = {'form': form}
    return render(request, 'photo_app/edit_photo.html', context)


def editGallery(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    form = GalleryForm(request.POST or None, instance=gallery)

    if form.is_valid():
        form.save()
        return redirect('gallery-detail', gallery_id)
    
    context = {'form': form}
    return render(request, 'photo_app/edit_gallery.html', context)

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            photographer = Photographer.objects.create(user=user,)
            gallery = Gallery.objects.create()
            photographer.gallery = gallery
            photographer.gallery.title = username
            photographer.name = username
            photographer.user = user
            photographer.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context ={'form':form}
    return render(request, 'registration/register.html', context)
