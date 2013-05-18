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
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))

	servicios = Servicio.objects.all()
	banners = Banner.objects.all()
	eventos_lista = Evento.objects.all().order_by('id').reverse()

	paginator = Paginator(eventos_lista, 6)
	page = request.GET.get('page')
	try:
		eventos = paginator.page(page)
	except PageNotAnInteger:
		eventos = paginator.page(1)
	except EmptyPage:
		eventos = paginator.page(paginator.num_pages)

	return render_to_response('eventos.html', {'eventos': eventos, 'servicios': servicios,
		'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners}, context_instance=RequestContext(request))

def detalle_evento(request, id_evento):
	#hay que definir la cantidad de publicidades que vamos a mostrar en esta seccion
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()

	evento = get_object_or_404(Evento, pk= id_evento)

	return render_to_response('detalle_evento.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'evento': evento, 'servicios': servicios}, context_instance= RequestContext(request))


def carteleras(request):
	
	#hay que definir la cantidad de publicidades que vamos a mostrar en esta seccion
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	
	delta30d = timedelta(days=30)
	
	cartelera_lista= Cartelera.objects.filter(fecha__gt=date.today()-delta30d).order_by('id').reverse()
	paginador = Paginator(cartelera_lista, 6)
	page = request.GET.get('page')

	try:
		cartelera = paginador.page(page)
	except PageNotAnInteger:
		cartelera = paginador.page(1)
	except EmptyPage:
		cartelera = paginador.page(paginador.num_pages)

	return render_to_response('carteleras.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'carteleras': cartelera, 'servicios': servicios}, context_instance=RequestContext(request))

def detalle_cartelera(request, id_cartelera):
	#hay que definir la cantidad de publicidades que vamos a mostrar en esta seccion
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	cartelera = get_object_or_404(Cartelera, pk= id_cartelera)
	
	return render_to_response('detalle_cartelera.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'cartelera': cartelera, 'servicios': servicios}, context_instance= RequestContext(request))

def noches(request):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	noches= Noche.objects.all()

	return render_to_response('noches.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'noches': noches, 'servicios': servicios}, context_instance=RequestContext(request))

def detalle_noche(request, id_noche):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	noche = get_object_or_404(Noche, pk= id_noche)
	
	return render_to_response('detalle_noche.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'noche': noche, 'servicios': servicios}, context_instance= RequestContext(request))

def galerias(request):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	galerias = Galeria.objects.all()

	return render_to_response('galerias.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'galeria': galeria, 'servicios': servicios}, context_instance=RequestContext(request))

def detalle_galeria(request, id_galeria):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	servicios= Servicio.objects.all()
	banners = Banner.objects.all()
	galeria = get_object_or_404(Galeria, pk= id_galeria)

	return render_to_response('detalle_galeria.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'galeria': galeria, 'servicios': servicios}, context_instance= RequestContext(request))

def comentarios(request):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()
	comentarios= Comentario.objects.all()

	return render_to_response('comentarios.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'comentarios': comentarios, 'servicios': servicios}, context_instance=RequestContext(request))

def detalle_servicio(request, id_servicio):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()
	comercios= Comercio.objects.filter(tipo_servicio= id_servicio)

	return render_to_response('detalle_servicio.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'comercios': comercios, 'servicios': servicios}, context_instance=RequestContext(request))

def detalle_comercio(request, id_comercio):
	p_p = Publicidad.objects.filter(tipo = 'P')[:8]
	p_v = random.shuffle(list(Publicidad.objects.filter(tipo = 'V')))
	p_h = random.shuffle(list(Publicidad.objects.filter(tipo = 'H')))
	banners = Banner.objects.all()
	servicios= Servicio.objects.all()
	comercio= get_object_or_404(Comercio, pk= id_comercio)
	
	return render_to_response('detalle_comercio.html', {'p_p': p_p, 'p_v': p_v, 'p_h': p_h, 'banners': banners, 'comercio': comercio, 'servicios': servicios}, context_instance= RequestContext(request))

def contacto(request):
	subject = 'Nuevo comentario de: %s' % request.POST['nombre']
	body = 'Mensaje: %s' % request.POST['mensaje']
	send_mail(subject, body, 'contacto@todoeventoschaco.com', ['todo_eventoschaco@live.com'])
	return HttpResponseRedirect('/eventos/')