# Generated by Django 5.2.dev20241007133657 on 2024-12-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_alter_order_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
