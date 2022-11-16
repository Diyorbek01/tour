# Generated by Django 4.1.3 on 2022-11-16 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
