# Generated by Django 4.2.3 on 2023-08-10 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gamer_name',
            new_name='username',
        ),
    ]