# Generated by Django 4.0.6 on 2022-07-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_nftcar_earned_money_nftcar_rent_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcar',
            name='paid_out',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
