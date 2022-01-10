# Generated by Django 3.0.6 on 2020-05-20 18:20

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(
                blank=True, null=True, upload_to='profile_pictures/', verbose_name='ProfilePicture'
            ),  # noqa
        ),
    ]
