# Generated by Django 4.2.6 on 2023-11-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0003_remove_gallery_contact_email_remove_gallery_isactive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]