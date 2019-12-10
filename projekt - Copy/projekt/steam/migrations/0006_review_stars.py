# Generated by Django 2.2.8 on 2019-12-09 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0005_developer_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]