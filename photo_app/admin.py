from django.contrib import admin
from .models import *

# Register your models here so they can be edited in admin panel.
admin.site.register(Photographer)
admin.site.register(Gallery)
admin.site.register(Photo)