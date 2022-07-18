# Generated by Django 4.0.6 on 2022-07-10 10:36

import admin_panel.database.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_carmodel_nftcar_delete_car_alter_user_owned_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcar',
            name='picture',
            field=models.ImageField(default='en', upload_to=admin_panel.database.models._create_photo_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='languge',
            field=models.CharField(choices=[('en', 'En'), ('ru', 'Ru')], default='en', max_length=2),
        ),
    ]