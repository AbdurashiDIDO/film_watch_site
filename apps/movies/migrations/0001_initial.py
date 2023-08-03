# Generated by Django 4.2.1 on 2023-08-02 17:55

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('is_approved', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug_link', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=['name'])),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-view_at'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_poster', models.CharField(blank=True, max_length=255, null=True)),
                ('poster', models.CharField(blank=True, max_length=255, null=True)),
                ('ru_title', models.CharField(blank=True, max_length=255, null=True)),
                ('orig_title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('runtime', models.PositiveIntegerField(blank=True, null=True)),
                ('vote', models.FloatField(blank=True, null=True)),
                ('vote_count', models.PositiveIntegerField(blank=True, null=True)),
                ('iframe_src', models.CharField(max_length=255, unique=True)),
                ('translate', models.CharField(blank=True, max_length=255, null=True)),
                ('max_quality', models.PositiveIntegerField(blank=True, null=True)),
                ('imdb_id', models.CharField(blank=True, max_length=25, null=True)),
                ('kinopoisk_id', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('slug_link', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='ru_title', unique_with=['ru_title'])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('content_title', models.CharField(max_length=255)),
                ('content_url', models.URLField()),
                ('content_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
    ]
