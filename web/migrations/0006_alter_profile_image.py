# Generated by Django 4.2.3 on 2023-08-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_profile_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to=''),
        ),
    ]