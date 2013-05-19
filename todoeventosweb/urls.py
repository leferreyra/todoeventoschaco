from django.conf.urls import patterns, include, url
from django.contrib import admin
from todoeventosweb import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', "todoeventos.views.eventos"),

   	url(r'^carteleras/(?P<id_cartelera>\d+)$', 'todoeventos.views.detalle_cartelera'),
   	url(r'^carteleras/' , 'todoeventos.views.carteleras'),
   	url(r'^noches/(?P<id_noche>\d+)$', 'todoeventos.views.detalle_noche'),
   	url(r'^noches/' , 'todoeventos.views.noches'),
    url(r'^galerias/(?P<id_social>\d+)$' , 'todoeventos.views.detalle_galeria'),
    url(r'^galerias/' , 'todoeventos.views.galerias'),
    url(r'^comentarios/' , 'todoeventos.views.comentarios'),
    url(r'^comercios/(?P<id_comercio>\d+)$' , 'todoeventos.views.detalle_comercio'),
    url(r'^servicios/(?P<id_servicio>\d+)$' , 'todoeventos.views.detalle_servicio'),    
    url(r'contacto', 'todoeventos.views.contacto'),

   	
)

# servir archivos estaticos en servidor de desarrollo
if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
          'document_root': settings.MEDIA_ROOT,}),
        )
