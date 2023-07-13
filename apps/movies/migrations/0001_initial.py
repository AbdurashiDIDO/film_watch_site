# Generated by Django 4.2.1 on 2023-07-13 18:48

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug_link', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['name'])),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_poster', models.CharField(blank=True, max_length=255, null=True)),
                ('poster', models.CharField(blank=True, max_length=255, null=True)),
                ('ru_title', models.CharField(max_length=255)),
                ('orig_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('runtime', models.PositiveIntegerField()),
                ('vote', models.FloatField()),
                ('vote_count', models.PositiveIntegerField()),
                ('release_date', models.CharField(blank=True, max_length=15, null=True)),
                ('iframe_src', models.CharField(max_length=255, unique=True)),
                ('translate', models.CharField(blank=True, max_length=255, null=True)),
                ('max_quality', models.PositiveIntegerField(blank=True, null=True)),
                ('imdb_id', models.CharField(max_length=25)),
                ('kinopoisk_id', models.CharField(max_length=25)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('slug_link', autoslug.fields.AutoSlugField(editable=False, populate_from='ru_title', unique_with=['ru_title'])),
                ('genre', models.ManyToManyField(blank=True, related_name='genre', to='movies.genre')),
            ],
            options={
                'unique_together': {('ru_title', 'orig_title')},
            },
        ),
    ]
