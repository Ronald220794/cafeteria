# Generated by Django 3.1.3 on 2020-11-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ProductoId', models.AutoField(db_column='producto_id', primary_key=True, serialize=False, unique=True)),
                ('ProductoNomb', models.CharField(db_column='producto_nomb', max_length=50)),
                ('ProductoDesc', models.CharField(db_column='producto_desc', max_length=100, unique=True)),
                ('ProductoPrecio', models.DecimalField(db_column='producto_precio', decimal_places=2, max_digits=8)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updatedAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 't_productos',
            },
        ),
    ]
