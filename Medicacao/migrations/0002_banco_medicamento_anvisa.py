# Generated by Django 3.1.5 on 2021-02-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco_Medicamento_Anvisa',
            fields=[
                ('id_anvisa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(verbose_name='Nome Medicamento')),
            ],
        ),
    ]
