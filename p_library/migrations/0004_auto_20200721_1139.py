# Generated by Django 2.2.6 on 2020-07-21 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200715_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('data', models.CharField(max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
                ('books', models.ManyToManyField(blank=True, related_name='books', to='p_library.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='friend_reader',
            field=models.ManyToManyField(blank=True, related_name='book_reader', to='p_library.Friend'),
        ),
    ]
