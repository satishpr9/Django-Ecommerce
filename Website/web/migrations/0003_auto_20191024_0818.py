# Generated by Django 2.2.5 on 2019-10-24 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20191024_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Subject',
            new_name='subject',
        ),
    ]
