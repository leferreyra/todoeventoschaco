from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


   	url(r'^eventos/(?P<id_evento>\d+)$', 'todoeventos.views.detalle_evento'),
    url(r'^$', "todoeventos.views.eventos"),
   	url(r'^cartelera/(?P<id_cartelera>\d+)$', 'todoeventos.views.detalle_cartelera'),
   	url(r'^carteleras/' , 'todoeventos.views.carteleras'),
   	url(r'^noche/(?P<id_noche>\d+)$', 'todoeventos.views.detalle_noche'),
   	url(r'^noches/' , 'todoeventos.views.noches'),
    url(r'^galeria/(?P<id_social>\d+)$' , 'todoeventos.views.detalle_galeria'),
    url(r'^galerias/' , 'todoeventos.views.galerias'),
    url(r'^comentarios/' , 'todoeventos.views.comentarios'),
    url(r'^comercio/(?P<id_comercio>\d+)$' , 'todoeventos.views.detalle_comercio'),
    url(r'^servicio/(?P<id_servicio>\d+)$' , 'todoeventos.views.detalle_servicio'),    
    url(r'contacto', 'todoeventos.views.contacto'),
   	
)