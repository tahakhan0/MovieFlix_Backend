# Generated by Django 3.0.8 on 2020-07-04 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieService', '0002_remove_movies_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='movieService.Genres'),
        ),
    ]