# Generated by Django 4.1.7 on 2023-03-02 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                # ('capacity', models.DecimalField(null=True, blank=True, decimal_places=0, max_digits=4)),
                # ('eqiupment', models.CharField(null=True, blank=True, max_length=200)),
                # ('disabledFriendly', models.BooleanField(null=True, blank=False)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.building')),
                # ('floor', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rezerwujacy', models.CharField(max_length=64)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.building')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
