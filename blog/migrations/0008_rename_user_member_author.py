# Generated by Django 4.2.2 on 2023-07-02 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_category_options_member_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='user',
            new_name='author',
        ),
    ]