#encoding:utf-8

from django.db import models

class Servicio(models.Model):
	nombre = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.nombre

class Comercio(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=50)
	email = models.EmailField()
	descripcion = models.TextField()
	url_del_album = models.CharField(max_length=500)
	tipo_servicio = models.ManyToManyField(Servicio)


	def __unicode__(self):
		return self.nombre


class Publicidad(models.Model):

	VERTICAL = 'V'
	HORIZONTAL = 'H'
	PRINCIPAL = 'P'

	TIPO_CHOICES = (
		(VERTICAL, 'Vertical'),
		(HORIZONTAL, 'Horizontal'),
		(PRINCIPAL, 'Principal')
	)
	
	nombre = models.CharField(max_length=50, unique=True)
	url_imagen_publicidad = models.CharField(max_length=500)
	tipo = models.CharField(max_length=50, choices = TIPO_CHOICES, null = False)

	def __unicode__(self):
		return self.nombre + "(" + self.tipo + ")"


class Cartelera(models.Model):
	nombre = models.CharField(max_length=100)
	lugar = models.CharField(max_length=100)
	fecha = models.DateField()
	descripcion= models.TextField()
	url_afiche_cartelera = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre


class Evento(models.Model):
	nombre = models.CharField(max_length=100)
	fecha = models.DateField()
	descripcion = models.TextField()
	url_del_album = models.CharField(max_length=500)
	url_del_video = models.CharField(max_length=500, blank=True, null=True)
	video_como_portada = models.BooleanField()

	def __unicode__(self):
		return self.nombre

class Noche(models.Model):
	nombre = models.CharField(max_length=100)
	fecha = models.DateField()
	url_del_album = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

	def descripcion(self):
		return self.fecha

class Galeria(models.Model):
	nombre = models.CharField(max_length=100)
	fecha = models.DateField()
	descripcion = models.TextField()
	url_del_album = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

class Banner(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=140)
	url_imagen_del_banner = models.CharField(max_length=500)

	def __unicode__(self):
		return self.titulo
