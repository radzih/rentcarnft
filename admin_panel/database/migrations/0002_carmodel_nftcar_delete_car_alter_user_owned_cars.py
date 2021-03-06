# Generated by Django 4.0.6 on 2022-07-09 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NFTCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('token_id', models.IntegerField()),
                ('owned', models.BooleanField(default=False)),
                ('part', models.IntegerField()),
                ('secret_code', models.CharField(max_length=200)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.carmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AlterField(
            model_name='user',
            name='owned_cars',
            field=models.ManyToManyField(blank=True, to='database.nftcar'),
        ),
    ]
