# Generated by Django 5.0.3 on 2024-04-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_checkout_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]
