# Generated by Django 4.2.8 on 2024-01-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiceapp', '0004_product_tbl_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tbl',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
