# Generated by Django 4.2.2 on 2023-07-23 12:41

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_myrating_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='published',
        ),
        migrations.AddField(
            model_name='myrating',
            name='published',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True),
        ),
    ]