# Generated by Django 5.0 on 2024-10-02 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izr_media', '0009_remove_prayercalculationconfig_calculation_method_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogparagraph',
            name='header',
        ),
        migrations.RemoveField(
            model_name='blogimage',
            name='blog_post',
        ),
        migrations.RemoveField(
            model_name='blogimage',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='blogparagraph',
            name='blog_post',
        ),
        migrations.CreateModel(
            name='ContentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('content_type', models.CharField(choices=[('header', 'Header'), ('paragraph', 'Paragraph'), ('image', 'Image')], max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_items', to='izr_media.blog')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.DeleteModel(
            name='BlogHeader',
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
        migrations.DeleteModel(
            name='BlogParagraph',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]