# Generated by Django 5.0.3 on 2024-04-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fasad', 'Fasad'), ('Sokol', 'Sokol'), ('Forma', 'Forma')], max_length=155),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]