# Generated by Django 4.2.8 on 2024-01-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_buy_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct_buy',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
