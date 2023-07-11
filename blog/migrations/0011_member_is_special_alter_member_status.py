# Generated by Django 4.2.2 on 2023-07-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_member_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(choices=[('P', 'انتشار'), ('D', 'پیش نویس'), ('I', 'درحال بررسی'), ('B', 'برگشت داده\u200cشده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]