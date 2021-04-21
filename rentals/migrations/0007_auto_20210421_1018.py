# Generated by Django 3.2 on 2021-04-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_auto_20210420_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationattachment',
            name='AppID',
        ),
        migrations.RemoveField(
            model_name='applicationattachment',
            name='propty',
        ),
        migrations.AlterField(
            model_name='propertyphoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/propertydetail', verbose_name='Browse photo to upload'),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='ApplicationAttachment',
        ),
    ]
