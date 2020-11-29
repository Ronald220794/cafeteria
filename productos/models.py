from django.db import models

# Create your models here.
class Producto(models.Model):
    ProductoId = models.AutoField(db_column='producto_id',primary_key=True, null=False, unique=True)
    ProductoNomb = models.CharField(db_column='producto_nomb', max_length=50)
    ProductoDesc= models.CharField(db_column='producto_desc', null=False, unique=True, max_length=100)
    ProductoPrecio = models.DecimalField(db_column='producto_precio', max_digits=8, decimal_places=2)
    # Campos para auditoria
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)
    estado = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 't_productos'