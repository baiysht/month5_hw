# Generated by Django 5.1.6 on 2025-02-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_remove_moviesreviews_reviews_moviesreviews_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesreviews',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='movie_app.review'),
        ),
    ]
