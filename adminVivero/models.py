from django.db import models
from .choices import tipo_labor as tl

# Modelo Productor
class Productor(models.Model):
    documento_productor = models.IntegerField(
        verbose_name="numero identificacion productor", primary_key=True, null=False
    )
    nombres_productor = models.CharField(
        max_length=100, verbose_name="Nombres productor", null=False
    )
    apellidos_productor = models.CharField(
        max_length=100, verbose_name="Apellidos productor", null=False
    )
    telefono_productor = models.CharField(
        max_length=50, verbose_name="Telefono productor", null=False
    )
    correo_productor = models.EmailField(
        max_length=254, verbose_name="Email productor", null=False
    )

# Modelo Finca que se relaciona con productores
class Finca(models.Model):
    numero_catastro = models.CharField(
        max_length=100,
        verbose_name="Número de catastro de la finca",
        primary_key=True,
        null=False,
    )
    municipio_ubicacion = models.CharField(
        max_length=100, verbose_name="Municipio de ubicación finca", null=False
    )

    documento_productor = models.ForeignKey(
        Productor, null=False, blank=False, on_delete=models.CASCADE
    )

# Modelo Vivero que se relaciona con fincas
class Vivero(models.Model):
    codigo_vivero = models.CharField(
        max_length=100,
        verbose_name="Número de identificación del vivero",
        primary_key=True,
        null=False,
    )
    cultivo_vivero = models.CharField(
        max_length=100, verbose_name="Cultivo del vivero", null=False
    )

    numero_catastro = models.ForeignKey(
        Finca, null=False, blank=False, on_delete=models.CASCADE
    )

# Modelo Producto 
class Producto(models.Model):
    registro_ICA = models.IntegerField(
        primary_key=True, verbose_name="Registro ICA colombia"
    )
    nombre_producto = models.CharField(
        max_length=100, null=False, verbose_name="Nombre del producto"
    )
    aplicacion_producto = models.IntegerField(
        verbose_name="Frecuencia de aplicación", null=False
    )
    valor_producto = models.FloatField(
        verbose_name="Precio del producto en COP", null=False
    )

# Modelo Tarea que se relaciona con los productos y los viveros involucrados en una labor
class Tarea(models.Model):
    fecha_labor = models.DateField(
        null=False, verbose_name="Fecha de inicio de la labor"
    )
    tipo_labor = models.CharField(max_length=100, choices=tl, null=False)
    descripcion_labor = models.CharField(
        max_length=500, verbose_name="Descripción de la labor", null=False
    )
    nombre_hongo = models.CharField(
        max_length=100, verbose_name="Nombre del hongo", null=True, blank=True
    )
    periodo_carencia = models.IntegerField(
        verbose_name="Periodo de carencia", null=True, blank=True
    )
    fecha_aplicacion = models.DateField(
        verbose_name="Fecha de aplicación fertilizante", null=True, blank=True
    )

    codigo_vivero = models.ForeignKey(
        Vivero, null=False, blank=False, on_delete=models.CASCADE
    )
    registro_ICA = models.ForeignKey(
        Producto, null=False, blank=False, on_delete=models.CASCADE
    )
