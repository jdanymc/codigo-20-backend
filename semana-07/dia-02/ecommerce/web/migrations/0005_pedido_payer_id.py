# Generated by Django 3.2 on 2023-06-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_pedido_direccion_envio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='payer_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
