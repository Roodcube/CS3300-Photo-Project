from django.forms import ModelForm
from .models import Photo, Gallery


#create class for project form
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields =('title','picture', 'altText', 'about')

#create class for portfolio form
class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"