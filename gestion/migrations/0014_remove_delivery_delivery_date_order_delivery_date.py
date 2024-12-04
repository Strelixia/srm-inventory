# Generated by Django 5.2.dev20241007133657 on 2024-12-04 10:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0013_alter_delivery_delivery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_date',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
