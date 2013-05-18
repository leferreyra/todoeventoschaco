from django.conf.urls import patterns, include, url
from todoeventosweb import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', "todoeventos.views.eventos"),
<<<<<<< HEAD
   	url(r'^carteleras/(?P<id_cartelera>\d+)$', 'todoeventos.views.detalle_cartelera'),
=======
   	url(r'^evento/(?P<id_evento>\d+)$', 'todoeventos.views.detalle_evento'),
   	url(r'^cartelera/(?P<id_cartelera>\d+)$', 'todoeventos.views.detalle_cartelera'),
>>>>>>> f6135519d985ae9016b9331487bece516029d094
   	url(r'^carteleras/' , 'todoeventos.views.carteleras'),
   	url(r'^noches/(?P<id_noche>\d+)$', 'todoeventos.views.detalle_noche'),
   	url(r'^noches/' , 'todoeventos.views.noches'),
    url(r'^galerias/(?P<id_social>\d+)$' , 'todoeventos.views.detalle_galeria'),
    url(r'^galerias/' , 'todoeventos.views.galerias'),
    url(r'^comentarios/' , 'todoeventos.views.comentarios'),
<<<<<<< HEAD
    url(r'^comercios/(?P<id_comercio>\d+)$' , 'todoeventos.views.detalle_comercio'),
    url(r'^servicios/(?P<id_servicio>\d+)$' , 'todoeventos.views.detalle_servicio'),    
    url(r'contacto', 'todoeventos.views.contacto'),
=======
    url(r'^comercio/(?P<id_comercio>\d+)$' , 'todoeventos.views.detalle_comercio'),
    url(r'^servicio/(?P<id_servicio>\d+)$' , 'todoeventos.views.detalle_servicio'),    
    url(r'^contacto', 'todoeventos.views.contacto'),
>>>>>>> f6135519d985ae9016b9331487bece516029d094
   	
)

# servir archivos estaticos en servidor de desarrollo
if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
          'document_root': settings.MEDIA_ROOT,}),
        )
