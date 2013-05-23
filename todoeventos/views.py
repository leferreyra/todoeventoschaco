from todoeventos.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import *
import random


def eventos(request):
	#random.shuffle desordena la lista, para obtener siempre publicidades distintas
	#hay que definir la cantidad de publicidades principales que vamos a mostrar
	p_p = Publicidad.objects.filter(tipo = 'P')[:7]

	# random.shuffle() no devuelve nada, solo mezcla la lista

	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)

	servicios = Servicio.objects.all()
	banners = Banner.objects.all()
	chicas = Galeria.objects.get(pk=1)

	eventos_lista = Evento.objects.all().order_by('id').reverse()

	paginator = Paginator(eventos_lista, 6)
	page = request.GET.get('page')
	try:
		articulos = paginator.page(page)
	except PageNotAnInteger:
		articulos = paginator.page(1)
	except EmptyPage:
		articulos = paginator.page(paginator.num_pages)


	return render_to_response('lista_articulos.html', 
		{
			'chicas': chicas, 
			'articulos': articulos, 
			'articulo_base_url': 'evento',
			'menu_activo': 'eventos',
			'banners':banners, 
			'servicios': servicios, 
			'p_p': p_p, 
			'p_v': p_v, 
			'p_h': p_h
		}, 
		context_instance=RequestContext(request))


def detalle_evento(request, id_evento):
	#hay que definir la cantidad de publicidades que vamos a mostrar en esta seccion
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]

	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)

	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	
	evento = get_object_or_404(Evento, pk=id_evento)

	return render_to_response('detalle_articulo.html', 
		{
			'articulo': evento, 
			'menu_activo': 'eventos',
			'servicios': servicios, 
			'p_p': p_p, 
			'p_v': p_v, 
			'p_h': p_h
		}, 
		context_instance=RequestContext(request))


def carteleras(request):
	
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]

	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)

	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	chicas = Galeria.objects.get(pk=1)

	
	delta30d = timedelta(days=30)
	
	cartelera_lista= Cartelera.objects.filter(fecha__gt=date.today()-delta30d).order_by('id').reverse()
	paginador = Paginator(cartelera_lista, 6)
	page = request.GET.get('page')

	try:
		articulos = paginador.page(page)
	except PageNotAnInteger:
		articulos = paginador.page(1)
	except EmptyPage:
		articulos = paginador.page(paginador.num_pages)

	return render_to_response('lista_articulos.html', 
		{
			'chicas': chicas,
			'articulos': articulos, 
			'articulo_base_url': 'cartelera',
			'menu_activo': 'cartelera',
			'banners':banners, 
			'servicios': servicios, 
			'p_p': p_p, 
			'p_v': p_v, 
			'p_h': p_h
		}, 
		context_instance=RequestContext(request))

def detalle_cartelera(request, id_cartelera):
	#hay que definir la cantidad de publicidades que vamos a mostrar en esta seccion
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	cartelera = get_object_or_404(Cartelera, pk= id_cartelera)
	
	return render_to_response('detalle_cartelera.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'cartelera': cartelera, 'servicios': servicios}, context_instance= RequestContext(request))

def noches(request):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	chicas = Galeria.objects.get(pk=1)
	noches= Noche.objects.all().order_by('id').reverse()

	paginador = Paginator(noches, 6)
	page = request.GET.get('page')

	try:
		articulos = paginador.page(page)
	except PageNotAnInteger:
		articulos = paginador.page(1)
	except EmptyPage:
		articulos = paginador.page(paginador.num_pages)

	return render_to_response('lista_articulos.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'articulos': articulos, 'servicios': servicios, 'chicas': chicas, 'articulo_base_url': 'noche', 'menu_activo': 'noche'}, context_instance=RequestContext(request))

def detalle_noche(request, id_noche):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	noche = get_object_or_404(Noche, pk= id_noche)
	
	return render_to_response('detalle_articulo.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'articulo': noche, 'servicios': servicios}, context_instance= RequestContext(request))

def galerias(request):

	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)

	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	chicas = Galeria.objects.get(pk=1)

	galeria_lista = Galeria.objects.exclude(pk=1).order_by('id').reverse()

	paginador = Paginator(galeria_lista, 6)
	page = request.GET.get('page')

	try:
		articulos = paginador.page(page)
	except PageNotAnInteger:
		articulos = paginador.page(1)
	except EmptyPage:
		articulos = paginador.page(paginador.num_pages)

	return render_to_response('lista_articulos.html', 
		{
			'chicas': chicas,
			'articulos': articulos, 
			'articulo_base_url': 'galeria',
			'menu_activo': 'galeria',
			'banners':banners, 
			'servicios': servicios, 
			'p_p': p_p, 
			'p_v': p_v, 
			'p_h': p_h
		}, 
		context_instance=RequestContext(request))

def detalle_galeria(request, id_galeria):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	galeria = get_object_or_404(Galeria, pk= id_galeria)

	return render_to_response('detalle_galeria.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'galeria': galeria, 'servicios': servicios}, context_instance= RequestContext(request))

def comentarios(request):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()

	return render_to_response('comentarios.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'comentarios': comentarios, 'servicios': servicios, 'menu_activo': 'comentarios'}, context_instance=RequestContext(request))

def detalle_servicio(request, id_servicio):
	p_p = Publicidad.objects.filter(tipo = 'P')[:7]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()
	comercios= Comercio.objects.filter(tipo_servicio= id_servicio)

	return render_to_response('servicio.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'comercios': comercios, 'servicios': servicios, 'menu_activo': 'servicios'}, context_instance=RequestContext(request))

def detalle_comercio(request, id_comercio):
	p_p = Publicidad.objects.filter(tipo = 'P')[:7]
	p_v = list(Publicidad.objects.filter(tipo = 'V'))
	random.shuffle(p_v)

	p_h = list(Publicidad.objects.filter(tipo = 'H'))	
	random.shuffle(p_h)
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()
	comercio= get_object_or_404(Comercio, pk= id_comercio)
	
	return render_to_response('detalle_articulo.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'articulo': comercio, 'servicios': servicios, 'menu_activo': 'servicios'}, context_instance= RequestContext(request))
