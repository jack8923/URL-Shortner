# Generated by Django 3.1.4 on 2020-12-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shorturl',
            old_name='original_erl',
            new_name='original_url',
        ),
    ]
