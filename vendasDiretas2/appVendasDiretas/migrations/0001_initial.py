# Generated by Django 5.0.1 on 2024-03-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=264, unique=True)),
                ('area', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
