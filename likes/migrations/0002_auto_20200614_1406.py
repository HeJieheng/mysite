# Generated by Django 3.0.5 on 2020-06-14 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecount',
            old_name='like_num',
            new_name='liked_num',
        ),
    ]
