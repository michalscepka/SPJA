# Generated by Django 2.2.8 on 2019-12-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0008_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
