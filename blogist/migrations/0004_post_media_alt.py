# Generated by Django 4.1.1 on 2022-09-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogist', '0003_rename_user_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media_alt',
            field=models.CharField(default='No alt text', max_length=100),
        ),
    ]
