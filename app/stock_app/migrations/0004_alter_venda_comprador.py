# Generated by Django 5.0.6 on 2024-06-27 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_alter_produto_preco_alter_produto_quantidade_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='comprador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_app.comprador'),
        ),
    ]
