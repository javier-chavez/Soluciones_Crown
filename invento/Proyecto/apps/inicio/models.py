from django.db import models
from django.utils import timezone

# Create your models here.

class Marca (models.Model):
	codigo = models.CharField(max_length=5,primary_key=True)
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	pais = models.CharField(max_length=20, blank=True)
	logo = models.ImageField (upload_to='foto_marca',blank=True)
	def __str__(self):
		return self.nombre


class Modelo (models.Model):
	marca = models.ForeignKey(Marca, null=False,blank=False)
	codigo = models.CharField(primary_key=True, max_length=20)
	nombre = models.CharField(max_length=50)
	tipo_modelo = models.CharField(max_length=50, default= 'Toyota')
	#VERIFICAR
	descripcion = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.nombre

class Master (models.Model):
	modelo = models.ForeignKey(Modelo, null=False,blank=False)
	codigo = models.CharField(primary_key=True, max_length=20)
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.nombre


class  Autor(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	descripcion = models.TextField (max_length=200)
	foto = models.ImageField (upload_to='foto_autor')


class Vehiculo (models.Model):
	#RELACIONES

	#RELACION DE UNO A MUCHOS UN VEHICULO SOLO PUEDE TENER UN MODELO, PERO UN MODELO PERTENECE A N VEHICULOS
	modelo = models.ForeignKey(Modelo, null=False,blank=False)


	chasis = models.CharField(primary_key=True, max_length=20)
	anioModelo = models.IntegerField ()
	anioCreacion = models.IntegerField ()
	produccion = models.CharField(max_length=20)
	motor = models.CharField(max_length=20)
	master = models.CharField(max_length=20)

	ubicacion = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	observacion = models.TextField()

#UNA RELACION DE MUCHOS A MUCHOS


#APP ubicacion




class Ubicacion (models.Model):
	TIPOS_UBICACION = (
	('DPST','Deposito'),
	('SWRM', 'Show Room'),
	('TLL', 'Taller'),
	('TRN', 'Transito'),
	('ZF', 'Zona Franca'),
	)
	DEPARTAMENTOS = (
	('LPZ','La Paz'),
	('CBB', 'Cochabamba'),
	('SC', 'Santa Cruz'),
	('BN', 'Beni'),
	('PN', 'Pando'),
	('TRJ', 'Tarija'),
	('PTS', 'Potosi'),
	('TRJ', 'Tarija'),
	('SUC', 'Sucre'),
	)
	codigo = models.CharField(max_length=10,primary_key=True)
	nombre = models.CharField(max_length=20)
	departamento = models.CharField(max_length=20,blank=True, choices= DEPARTAMENTOS)
	tipo = models.CharField(max_length=20,blank=True, choices= TIPOS_UBICACION)
	descripcion = models.CharField(max_length=50, blank=True)
	observacion =  models.TextField(blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.nombre

