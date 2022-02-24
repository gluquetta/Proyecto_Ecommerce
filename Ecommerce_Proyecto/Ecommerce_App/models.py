from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):

    id_producto = models.CharField(primary_key=True, max_length=255, unique=True, verbose_name="ID o Referencia de Producto (SKU)")
    titulo = models.CharField(max_length=150, verbose_name="Titulo de Producto")
    slug = models.SlugField(max_length=160, verbose_name="Producto Slug")
    descripcion_corta = models.TextField(verbose_name="Descripcion Corta")
    descripcion_detallada = models.TextField(blank=True, null=True, verbose_name="Descripcion Detallada")
    imagen_producto = models.ImageField(upload_to='producto', blank=True, null=True, verbose_name="Imagen Producto")
    stock = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    precio = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, unique=True, verbose_name="Product Categoy", on_delete=models.CASCADE)
    esta_activo = models.BooleanField(verbose_name="Esta Activo?")
    esta_destacado = models.BooleanField(verbose_name="Esta Destacado?")
    feccha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Actualizacion")

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos'
        ordenando = ('feccha_creacion', )

    def __str__(self):
        return self.titulo

    