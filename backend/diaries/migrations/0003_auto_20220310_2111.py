# Generated by Django 3.2.12 on 2022-03-10 12:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_rename_dairy_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flower',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]