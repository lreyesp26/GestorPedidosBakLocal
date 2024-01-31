# Generated by Django 5.0.1 on 2024-01-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('nombreusuario', models.CharField(max_length=300)),
                ('contrasenia', models.CharField()),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fechafin', models.DateTimeField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
                ('fotoperfil', models.BinaryField(blank=True, null=True)),
                ('estadocuenta', models.CharField(choices=[('0', '0'), ('1', '1')], max_length=1)),
                ('rol', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('X', 'X'), ('M', 'M'), ('D', 'D'), ('S', 'S')], max_length=1)),
                ('correorecuperacion', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detallepedidos',
            fields=[
                ('id_detallepedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('impuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('descuento', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'detallepedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meseros',
            fields=[
                ('id_mesero', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_registro', models.DateTimeField()),
                ('sestado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'meseros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tipo_de_pedido', models.CharField(max_length=1)),
                ('metodo_de_pago', models.CharField(max_length=1)),
                ('puntos', models.DecimalField(decimal_places=0, max_digits=3)),
                ('fecha_pedido', models.DateTimeField()),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado_del_pedido', models.CharField(max_length=1)),
                ('observacion_del_cliente', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidosmesa',
            fields=[
                ('id_pmesa', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pedidosmesa',
                'managed': False,
            },
        ),
    ]