# Generated by Django 3.2.5 on 2021-08-02 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_provider_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='lurrency',
            new_name='currency',
        ),
    ]
