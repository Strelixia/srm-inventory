# Generated by Django 5.2.dev20241007133657 on 2024-11-25 16:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_alter_payment_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
