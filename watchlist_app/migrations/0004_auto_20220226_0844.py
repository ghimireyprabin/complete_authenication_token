# Generated by Django 2.2.13 on 2022-02-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_rating',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='number_rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
