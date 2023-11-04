# Generated by Django 4.2.6 on 2023-11-02 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contact_email', models.CharField(max_length=200)),
                ('isActive', models.BooleanField(default=False)),
                ('about', models.TextField(blank=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.TextField(blank=True, verbose_name='')),
                ('gallery', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='photo_app.gallery')),
            ],
        ),
        migrations.AddField(
            model_name='photographer',
            name='gallery',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='photo_app.gallery'),
        ),
    ]
