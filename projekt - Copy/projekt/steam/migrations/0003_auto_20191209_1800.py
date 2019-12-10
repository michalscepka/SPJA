# Generated by Django 2.2.8 on 2019-12-09 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0002_auto_20191209_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='developer',
        ),
        migrations.AddField(
            model_name='developer',
            name='game',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='steam.Game'),
            preserve_default=False,
        ),
    ]
