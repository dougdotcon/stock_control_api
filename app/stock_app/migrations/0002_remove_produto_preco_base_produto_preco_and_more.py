# Generated by Django 5.0.6 on 2024-06-26 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_base',
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade_estoque',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='estoque_record', to='stock_app.produto'),
        ),
    ]
