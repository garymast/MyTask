# Generated by Django 4.2.8 on 2023-12-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tasks', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]