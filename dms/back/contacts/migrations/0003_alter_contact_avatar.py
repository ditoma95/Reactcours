# Generated by Django 4.2.7 on 2024-01-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_twitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]