# Generated by Django 4.2.2 on 2023-07-23 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_alter_myrating_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='published',
        ),
    ]
