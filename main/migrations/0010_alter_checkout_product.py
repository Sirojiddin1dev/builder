# Generated by Django 5.0.3 on 2024-04-20 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]