# Generated by Django 4.2.2 on 2023-07-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_member_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='category',
            field=models.ManyToManyField(null=True, related_name='articles', to='blog.category', verbose_name='دسته بندی ها'),
        ),
    ]
