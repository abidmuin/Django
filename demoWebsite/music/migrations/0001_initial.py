# Generated by Django 3.1 on 2020-08-25 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50, verbose_name='')),
                ('album_title', models.CharField(max_length=50, verbose_name='')),
                ('genre', models.CharField(max_length=50, verbose_name='')),
                ('album_logo', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10, verbose_name='')),
                ('song_title', models.CharField(max_length=50, verbose_name='')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
        ),
    ]