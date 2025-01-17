# Generated by Django 5.0 on 2024-09-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flyer', models.ImageField(upload_to='izr_media/')),
                ('flyer_ar', models.ImageField(upload_to='izr_media/')),
                ('flyerTV', models.ImageField(upload_to='izr_media/')),
                ('subtitle', models.TextField()),
                ('subtitle_ar', models.TextField()),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
