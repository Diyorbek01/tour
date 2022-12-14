# Generated by Django 4.1.3 on 2022-11-16 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('number_of_passengers', models.PositiveIntegerField(default=0)),
                ('flight_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.date')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.price')),
                ('tarif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tarif')),
            ],
        ),
    ]
