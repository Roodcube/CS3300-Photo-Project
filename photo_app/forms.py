from django.forms import ModelForm
from .models import Photo, Gallery
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

#create class for creating a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']