# Generated by Django 5.2.dev20241007133657 on 2024-12-06 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0022_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.product'),
            preserve_default=False,
        ),
    ]
