# Generated by Django 3.2 on 2021-04-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_application_applicationattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/', verbose_name='Browse photo to upload'),
        ),
    ]
