# Generated by Django 2.2.6 on 2020-07-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_remove_friend_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
