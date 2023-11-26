from django.urls import path, include
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

path('photographers/', views.PhotographerListView.as_view(), name= 'photographers'),
path('photographer/<int:pk>', views.PhotographerDetailView.as_view(), name='photographer-detail'),
path('gallery/<int:pk>', views.GalleryDetailView.as_view(), name='gallery-detail'),
path('photos/', views.PhotoListView.as_view(), name='photos'),
path('photo/<int:pk>', views.PhotoDetailView.as_view(), name='photo-detail'),

path('gallery/<int:gallery_id>/create_photo/', views.createPhoto, name='create_photo'),
path('gallery/<int:gallery_id>/delete_photo/<int:photo_id>', views.deletePhoto, name='delete_photo'),
path('gallery/<int:gallery_id>/edit_photo/<int:photo_id>', views.editPhoto, name='edit_photo'),
path('gallery/edit_gallery/<int:gallery_id>', views.editGallery, name='edit_gallery'),

path('accounts/register/', views.registerPage, name = 'register_page',)
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]