# Generated by Django 4.2.6 on 2023-11-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0002_gallery_photo_photographer_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='isActive',
        ),
        migrations.RemoveField(
            model_name='photographer',
            name='major',
        ),
        migrations.AddField(
            model_name='photo',
            name='altText',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]