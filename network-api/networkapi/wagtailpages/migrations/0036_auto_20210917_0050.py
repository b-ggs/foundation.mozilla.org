# Generated by Django 3.1.11 on 2021-09-17 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0035_auto_20210910_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='email',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='live_chat',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='twitter',
        ),
    ]
