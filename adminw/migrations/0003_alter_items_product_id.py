# Generated by Django 4.0 on 2022-01-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminw', '0002_alter_items_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Product_Id',
            field=models.IntegerField(max_length=10, unique=True),
        ),
    ]