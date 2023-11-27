from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    #contact_email = models.CharField(max_length=200)
    #isActive = models.BooleanField(default=False)
    about = models.TextField((""), blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('gallery-detail', args=[str(self.id)])

class Photographer(models.Model):


    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    gallery = models.OneToOneField(Gallery, null=True, on_delete=models.CASCADE, unique=True, default=None)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name


    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('photographer-detail', args=[str(self.id)])
    
class Photo(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(null=True)
    about = models.TextField((""), blank=True)
    altText = models.CharField(max_length=200, default="User Submitted Photo")
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, default = None)
    likes = models.ManyToManyField(User, related_name='photo_like')


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('photo-detail', args=[str(self.id)])
    def number_of_likes(self):
        return self.likes.count()
    
"""
# Model to represent the relationship between photos and Gallerys.
# Each instance of this model will have a reference to a Gallery and a Photo,
# creating a many-to-many relationship between Gallerys and photos.S
class PhotosInGallery(models.Model):


    #deleting a Gallery will delete associate photos
    Gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    #deleting a photo will not affect the Gallery
    #Just the entry will be removed from this table
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Meta:
#ensures that each photo is associated with only one Gallery
    unique_together = ('Gallery', 'photo')
"""