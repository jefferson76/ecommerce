# Generated by Django 4.2.2 on 2023-07-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qts_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
