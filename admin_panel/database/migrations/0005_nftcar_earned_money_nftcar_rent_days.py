# Generated by Django 4.0.6 on 2022-07-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcar',
            name='earned_money',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='nftcar',
            name='rent_days',
            field=models.IntegerField(default=0),
        ),
    ]
