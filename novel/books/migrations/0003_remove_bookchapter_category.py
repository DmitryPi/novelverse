# Generated by Django 3.2.13 on 2022-05-08 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookchapter_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookchapter',
            name='category',
        ),
    ]
