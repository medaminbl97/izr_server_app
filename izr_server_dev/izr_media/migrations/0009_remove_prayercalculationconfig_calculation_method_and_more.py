# Generated by Django 5.0 on 2024-10-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izr_media', '0008_blogpost_blogheader_blogparagraph_blogimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayercalculationconfig',
            name='calculation_method',
        ),
        migrations.AlterField(
            model_name='prayercalculationconfig',
            name='default_latitude',
            field=models.FloatField(default='49.007734'),
        ),
        migrations.AlterField(
            model_name='prayercalculationconfig',
            name='default_longitude',
            field=models.FloatField(default='12.102841'),
        ),
    ]
