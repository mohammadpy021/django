# Generated by Django 4.2.2 on 2023-07-22 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star_ratings', '0004_alter_rating_id_alter_userrating_id'),
        ('blog', '0018_remove_member_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ratings_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='star_ratings.userrating'),
        ),
    ]
