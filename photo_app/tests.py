from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class GalleryDetailViewTest(TestCase):
    def setUp(self):
        # Create a post for testing
        self.post = Gallery.objects.create(title='Test gallery', about='This is a test gallery')

    def test_gallery_detail_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        response = self.client.get(reverse('gallery-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photo_app/gallery_detail.html')
        self.assertContains(response, 'Test gallery')

#class PhotoDetailViewTest(TestCase):
#    def setUp(self):
#        # Create a post for testing
#        self.post = Photo.objects.create(title='Test Photo', about='This is a test photo', gallery=reverse('gallery-detail', args=[1]))
#
#    def test_photo_detail_view(self):
#        # Test that the post detail view returns a 200 status code,
#        # uses the correct template, and contains the post title
#        response = self.client.get(reverse('photo-detail', args=[self.post.id]))
#        self.assertEqual(response.status_code, 200)
#        self.assertTemplateUsed(response, 'photo_app/photo_detail.html')
#        self.assertContains(response, 'Test Photo')

# Create your tests here.
class PhotographerDetailViewTest(TestCase):
    def setUp(self):
        # Create a post for testing
        self.post = Photographer.objects.create(name='Test User')

    def test_photographer_detail_view(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        response = self.client.get(reverse('photographer-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photo_app/photographer_detail.html')
        self.assertContains(response, 'Test User')

class PhotographerFunctionTest(TestCase):
    def setUp(self):
        # Create a post for testing
        self.post = Photographer.objects.create(name='Test User')

    def test_photographer_function(self):
        # Test that the post detail view returns a 200 status code,
        # uses the correct template, and contains the post title
        #response = self.client.get(reverse('photographer-detail', args=[self.post.id]))
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'photo_app/photographer_detail.html')
        self.assertEquals(self.post.__str__(), 'Test User')
