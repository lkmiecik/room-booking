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
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.building')),
            ],
        ),
    ]
