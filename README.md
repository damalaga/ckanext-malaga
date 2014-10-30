ckanext-malaga
==============

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente.

ckanext-malaga es la extensión que hemos desarrollado para publicar el [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu)

##Funcionalidades implementadas:
* Carrusel de la pantalla principal con bootstrap.
* Federación de datos con datos.gob.es

###Instalación

* Conectase a la máquina con el usuario de ckan.
* Ir al directorio de instalación de la extensión (en nuestro caso):
<p>cd ckan/lib/default/src</p>
* Activar el entorno
<p>\. /usr/lib/ckan/default/bin/activate</p>
* Descargar e instalar la extensión:
<p>pip install -e git+git://github.com/damalaga/ckanext-malaga#egg=ckanext-malaga</p>

###Configuración
Añadir en el fichero .ini estas lineas y, a continuacion reiniciar apache2:
<pre>
<code>
#Añadimos la extension
ckan.plugins = .... malaga
#indica donde se encuentra la entrada "aplicaciones" del menú
ckan_mlg.apl_url = aplicaciones.html 
#################
#Ubicacion de los ficheros usados en el proceso de federacion
ckan_mlg.federador_rdf_write = #ubicacion del fichero federador que se va a rellenar (en nuestro caso es  /home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/theme/templates/local/federador.rdf)
ckan_mlg.federador_rdf_url = #URL del fichero federador que se va a recuperar sin generar (en nuestro caso es http://localhost/local/federador.rdf
ckan_mlg.federador_template = #ubicacion del rdf que se usa para la federacion( en nuestro caso es local/plantillafederacion.rdf)
ckan_mlg.federador_htmlresponse = #dejar vacío, desaparece en la siguiente version

#################
# Fichero de licencias
licenses_group_url = file:///home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/public/licencias.json
</code></pre>

##NOTAS

1. El tablero grupos/organizaciones de la pantalla principal no es compatible con Internet Explorer.
2. Los grupos y organizaciones están clasificados según nuestras necesidades, los iconos sólo aparecen si los grupos y organizaciones existen, en otro caso, no aparecerá ninguna imagen.

##GENERACIÓN DE federador.rdf:

Llamar a la siguiente URL para generar el fichero federador.rdf: http://dominio/local/generador. El resultado es el fichero federador.rdf que se escribe en la ruta indicada por la variable <code>ckan_mlg.federador_rdf_write</code> del fichero .ini

La ruta <code>ckan_mlg.federador_rdf_write</code> debe ser accesible vía web y no debe estar dentro del ámbito de ckan, para que el controlador de rdfs que trae CKAN no actúe en la llamada.
