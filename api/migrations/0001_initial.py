# Generated by Django 5.1 on 2024-11-15 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('cod', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('talle_peso', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=255)),
                ('stock', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('Id_Usuario', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id_tarjetas', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('Visa', models.CharField(default=0, max_length=255)),
                ('Nro_de_tarjeta', models.CharField(default=0, max_length=16)),
                ('Nro_de_seguridad', models.CharField(default=0, max_length=3)),
                ('Fecha_de_vencimiento', models.CharField(max_length=5)),
                ('Id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('Id_Compra', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField(default=0)),
                ('Fecha_Compra', models.DateField()),
                ('id_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.metodopago')),
                ('Id_Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
                ('Id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
    ]
