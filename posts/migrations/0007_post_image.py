# Generated by Django 3.2 on 2021-06-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_downvote_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='theme/static/default.png', upload_to='theme/static/images'),
        ),
    ]
