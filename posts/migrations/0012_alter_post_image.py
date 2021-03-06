# Generated by Django 3.2 on 2021-11-22 20:20

from django.db import migrations, models
import django_s3_storage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.png', storage=django_s3_storage.storage.S3Storage(aws_s3_bucket_name='zappa-zm3ayvkoi'), upload_to=''),
        ),
    ]
