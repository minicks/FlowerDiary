# Generated by Django 3.2.12 on 2022-03-24 03:42

import diaries.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0005_alter_diary_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=diaries.models.Diary.photo_upload_path),
        ),
    ]
