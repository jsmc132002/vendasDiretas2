# Generated by Django 5.0.1 on 2024-04-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVendasDiretas', '0006_alter_produto_codigo_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.CharField(max_length=264),
        ),
    ]
