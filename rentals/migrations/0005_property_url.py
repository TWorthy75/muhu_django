# Generated by Django 3.2 on 2021-04-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20210418_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='url',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]