
![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)
ckanext-malaga
==============

El [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) se ha implantado a partir de la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

<b>IMPORTANTE:</b>
Esta extensión funciona en versiones de CKAN iguales o mayores a 2.3 (CKAN responsive), para versiones anteriores esta versión <b>NO ESTÁ PROBADA</b>.

ckanext-malaga es la extensión que el Centro Municipal de Informática [CEMI](http://cemi.malaga.eu) ha desarrollado para adaptar la plataforma a las necesidades específicas del ayuntamiento.

## Instalación y configuración del portal de datos abiertos.
Los pasos para reproducir el portal de datos abiertos del Ayuntamiento de Málaga son los siguientes:
* Instalar Ubuntu 14.04.2.
* Instalar la última versión de CKAN disponible en formato "instalar desde fuente", las instrucciones se encuentran en este enlace [CKAN install from source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html).
* Seguir los pasos que explicamos a continuación.
* NOTA: Los iconos de grupos y organizaciones que proporcionamos en este repositorio se corresponde con la categorización requerida según la NTI (http://www.boe.es/boe/dias/2013/03/04/pdfs/BOE-A-2013-2380.pdf) y que son imprescindibles para la federación de los datos en (http://datos.gob.es/catalogo).

### Requisitos
* ckanext-malaga usa la extesión [ckanext-contacto](https://github.com/damalaga/ckanext-contacto), por lo que tiene que estar instalada también. Esta extensión permite crear un formulario de contacto y ha sido desarrollada por [Centro Municipal de Informática](http://cemi.malaga.eu)

### Descarga de la extensión

* Conectarse a la máquina de CKAN con el usuario de ckan.
* Ir al directorio de instalación de la extensión (en nuestro caso):
<p>cd ckan/lib/default/src</p>
* Clonar la extensión
<p>git clone https://github.com/damalaga/ckanext-malaga</p>
* Desplegarla
<p>python setup.py develop</p>

### Configuración de la extensión
Añadir la siguiente configuración en el fichero .ini y reiniciar apache2:
<pre>
<code>
Añadimos la extension en ckan.plugins
ckan.plugins = .... malaga

indica donde se encuentra la entrada "aplicaciones" del menú, en nuestro caso esta en el home y se llama aplicaciones.html
ckan_mlg.apl_url = aplicaciones.html 

#################

configuracion relacionada con el fichero de licencia
licenses_group_url = # Fichero de licencias en nuestro caso seria file:///home/ckan/ckan/lib/default/src/ckanext-malaga/ckanext/malaga/public/licencias.json
</code></pre>
</code>
</pre>

## Funcionalidades implementadas:
* Carrusel de la pantalla principal con bootstrap.
* Opción "aplicaciones" en el menú principal que abre una sección con el listado de aplicaciones que usan nuestros catálogo de datos.
* Tablero de grupos y organizaciones.
* Formulario de contacto usando la extensión ckanext-contacto.
* Modo responsive (compatible para móviles).


### Federación:

En versiones anteriores, la federación en datos.gob.es estaba incluída en el código de esta extensión.

A partir de esta versión, la federación es independiente a este módulo. La federación está disponible en [ckanext-federador](https://github.com/damalaga/ckanext-federador)

### Slides de carrusel:

El carrusel usa el módulo bootstrap que incluye CKAN.
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

### Tablero de grupos y organizaciones

Inicialmente se recopilan los grupos y organizaciones del portal. Cada grupo/organización tiene dos imágenes de 50x50 píxeles uno con el nombre del grupo/organización y otro fichero con el nombre del grupo/organización terminado en "on".

Las imágenes de los grupos y organizaciones están clasificados según nuestras necesidades, por lo que los iconos sólo aparecen si los grupos y organizaciones existen, en otro caso, no aparecerá ninguna imagen.

### Formulario de contacto
Los desarrolladores que usen nuestra API, pueden rellenar un formulario de contacto para que demos de alta su aplicación en nuestra página de "aplicaciones disponibles", para ello, hemos usado una extensión que hemos desarrollado y que está disponible en (https://github.com/damalaga/ckanext-contact)

=======
## Licencia:

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias! 


![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


