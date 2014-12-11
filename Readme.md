ckanext-malaga
==============

El [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) se ha implantado a partir de la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. Actualmente [http://datosabiertos.malaga.eu](http://datosabiertos.malaga.eu) tiene la versión CKAN 2.2.a.

ckanext-malaga es la extensión que hemos desarrollado para adaptar la plataforma a nuestras necesidades. Esto incluye dos funcionalidades principalmente.

##Funcionalidades implementadas:
* Carrusel de la pantalla principal con bootstrap.
* Federación de datos con datos.gob.es
* Entrada "aplicaciones" con el listado de aplicaciones que usan nuestros catálogo de datos.
* Tablero de grupos y organizaciones.

###Instalación de ckanext-malaga

* Conectarse a la máquina de CKAN con el usuario de ckan.
* Ir al directorio de instalación de la extensión (en nuestro caso):
<p>cd ckan/lib/default/src</p>
* Activar el entorno
<p>\. /usr/lib/ckan/default/bin/activate</p>
* Descargar e instalar la extensión:
<p>pip install -e git+git://github.com/damalaga/ckanext-malaga#egg=ckanext-malaga</p>

###Configuración
Añadir en el fichero .ini estas lineas y, a continuacion, reiniciar apache2:
<pre>
<code>
#Añadimos la extension en ckan.plugins
ckan.plugins = .... malaga

#indica donde se encuentra la entrada "aplicaciones" del menú, en nuestro caso esta en el home y se llama aplicaciones.html
ckan_mlg.apl_url = aplicaciones.html 
#################
#Configuracion relacionada con la federacion

ckan_mlg.federador_file = #fichero donde escribimos el fichero rdf federador (escribir ruta absoluta y el nombre del fichero con la extension.
ckan_mlg.federador_template = #ubicación de plantilla rdf que se usa en la federacion, en nuestro caso es local/plantillafederacion.rdf
ckan_mlg.federador_process =  #instrucción que lanza el generador de rdf, si queremos que se lance el federador al escribir la URL http://dominio/generador, escribiremos generador

# parametros propios de cada entidad
# datatime portal published
ckan_mlg.federador_datetime_pub = #fecha y hora de la publicacion del portal en formato AAAA-MM-DDTHH:MI:SS
ckan_mlg.federador_publisher = #etiqueta publisher
ckan_mlg.federador_spatial_res = #etiqueta spatial
ckan_mlg.federador_theme_tax = #etiqueta themeTaxonomy
ckan_mlg.license_res = #etiqueta license

#################

#configuracion relacionada con el fichero de licencia
licenses_group_url = # Fichero de licencias en nuestro caso seria file:///home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/public/licencias.json
</code>
</pre>

##PROCESO DE FEDERACIÓN:

El proceso que genera el fichero rdf puede llegar a tardar varios minutos, dependiendo del tamaño del catálogo de datos.

Por este motivo, hemos dividido el proceso en dos: en el primero se genera el fichero rdf y en el segundo se muestra el fichero que se ha generado previamente.
- Generación del fichero rdf: para ello será necesario llamar a la siguiente URL http://dominio/XXXXX, siendo XXXXX la orden que hemos configurado previamente con el parámetros <code>ckan_mlg.federador_process</code>. El resultado se escribe en la ruta y fichero que hemos configurado previamente en <code>ckan_mlg.federador_rdf_write</code> del fichero .ini
- Obtención del fichero rdf (previamente generado): El fichero se obtiene escribiendo la ruta que hemos configurado previamente en <code>ckan_mlg.federador_file</code>. Esta ruta debe ser accesible vía web y no debe estar dentro del ámbito de ckan, para que el controlador de rdfs que trae CKAN no actúe en la llamada.

##SLIDES DEL CARRUSEL:

El carrusel está implementado con el propio bootstrap que se incluye en la instalación de CKAN.
La configuración y uso de la misma está hecha según la documentación oficial de la misma.

El carrusel se compone de cinco slides, los tres primeros: recuento de recursos, etiquetas más populares y estadísticas, se generan periódicamente (cada día por ejemplo) mediante un cron que crea un html estático con el contenido del slide. Con esto evitamos consultar la información cada vez que se accede al home del portal.
El cron tiene las siguientes órdenes:
<pre>
<code>
wget http://URL/home/snippets/get_carousel_tags.html -O /home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/theme/templates/home/snippets/carousel_tags.html</code>
<code>
wget http://URL/home/snippets/get_carousel_stats.html -O /home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/theme/templates/home/snippets/carousel_stats.html</code>
<code>
wget http://URL/home/snippets/get_carousel_resources.html -O /home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/theme/templates/home/snippets/carousel_resources.html</code>
</pre>

Siendo get_carousel_XXXX.html el html que recopila la información y carousel_XXXX.html el contenido estático.

NOTA: Una vez instalado esta extensión, hay que ejecutar los tres ficheros html para que se rellenen con información, porque inicialmente están vacíos.

##TABLERO DE GRUPOS Y ORGANIZACIONES:

Inicialmente se recopilan los grupos y organizaciones del portal. Cada grupo/organización tiene dos imágenes de 50x50 píxeles uno con el nombre del grupo/organización y otro fichero con el nombre del grupo/organización terminado en "on".

Las imágenes de los grupos y organizaciones están clasificados según nuestras necesidades, por lo que los iconos sólo aparecen si los grupos y organizaciones existen, en otro caso, no aparecerá ninguna imagen.

##Licencia:

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias! 


![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)
