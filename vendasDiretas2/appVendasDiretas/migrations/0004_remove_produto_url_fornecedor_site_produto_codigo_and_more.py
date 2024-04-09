# Generated by Django 5.0.1 on 2024-03-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appVendasDiretas', '0003_cliente_produto_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='url',
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo',
            field=models.CharField(default=0, max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.URLField(unique=True),
        ),
    ]