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

\#Añadimos la extension
<p>ckan.plugins = .... malaga</p>

\#indica donde se encuentra la entrada "aplicaciones" del menú
<p>ckan_mlg.apl_url = aplicaciones.html </p>

\#################
<p>\#Ubicacion de los ficheros usados en el proceso de federacion
<p>\#ubicacion del fichero federador que se va a rellenar
<p>ckan_mlg.federador_rdf_write = /home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/theme/templates/local/federador.rdf
<p>\#URL del fichero federador que se va a recuperar sin generar
<p>ckan_mlg.federador_rdf_url = http://ckan20/local/federador.rdf
<p>\#ubicacion del rdf que se usa para la federacion
<p>ckan_mlg.federador_template = local/plantillafederacion.rdf
<p>\#################

\# Fichero de licencias
licenses_group_url = file:///home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/public/licencias.json


##NOTAS

1. El tablero grupos/organizaciones de la pantalla principal no es compatible con Internet Explorer.
2. Los grupos y organizaciones están clasificados según nuestras necesidades, los iconos sólo aparecen si los grupos y organizaciones existen, en otro caso, no aparecerá ninguna imagen.

