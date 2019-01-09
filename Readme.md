
![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

ckanext-malaga
==============

El [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) se ha implantado a partir de la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

ckanext-malaga es la extensión que el Centro Municipal de Informática [CEMI](http://cemi.malaga.eu) ha desarrollado para adaptar la plataforma a las necesidades específicas del ayuntamiento.

Hemos configurado el portal de datos abiertos para que el buscador de datasets de Google indexe nuestros conjuntos de datos (ver configuración más abajo en esta documentación)


## Instalación y configuración del portal de datos abiertos.
Los pasos para reproducir el portal de datos abiertos del Ayuntamiento de Málaga son los siguientes:
* Instalar Ubuntu 18.04.1.
* Instalar la última versión de CKAN disponible en formato "instalar desde fuente", las instrucciones se encuentran en este enlace [CKAN install from source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html).
* Seguir los pasos que explicamos a continuación.
* NOTA: Los iconos de grupos y organizaciones que proporcionamos en este repositorio se corresponde con la categorización requerida según la NTI (http://www.boe.es/boe/dias/2013/03/04/pdfs/BOE-A-2013-2380.pdf) y que son imprescindibles para la federación de los datos en (http://datos.gob.es/catalogo).

### Requisitos
Para el correcto funcionamiento de esta extensión son necesarios las siguientes extensiones:

* [ckanext-geoview](https://github.com/ckan/ckanext-geoview): que permite visualizar Geoespacialmente los datos geolocalizados.
* [ckanext-dcat](https://github.com/ckan/ckanext-dcat): para que Google Datasearch indexe los archivo
* [ckanext-federador](https://github.com/damalaga/ckanext-federador): con el que se consigue la federación de datos.gob.es
* [ckanext-contacto](https://github.com/damalaga/ckanext-contacto): extensión con la que se pueden enviar notificaciones a Datos Abiertos Málaga.


* Esta extensión funciona en versiones de CKAN iguales o mayores a 2.3 (CKAN responsive), no está probada en versiones anteriores.


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

## Federación

La federación del portal en datos.gob.es se hace ahora con una extensión independiente a esta que también ha sido desarrollada por el [CEMI](http://cemi.malaga.eu).

La federación está disponible en [ckanext-federador](https://github.com/damalaga/ckanext-federador)

## Indexación de los conjuntos de datos en el buscador de datasets de Google.

Google ha implementado un nuevo motor de búsqueda de conjuntos de datos llamado [Google Dataset Search](https://toolbox.google.com/datasetsearch) que facilita el acceso universal a los conjuntos de datos ubicados en los repositorios de internet.
Para que Google Dataset Search publique los conjuntos de datos de nuestro portal hemos seguido las instrucciones que proporciona el propio Google en la [Referencia de datos estructurados](https://developers.google.com/search/docs/data-types/dataset) 
así como los consejos que Red.es nos ofrece en el artículo [Google lanza un nuevo buscador de datos abiertos](http://datos.gob.es/es/noticia/google-lanza-un-nuevo-buscador-de-datos-abiertos)

Los pasos que hemos seguido son estos:
* Instalar el plugin [ckanext-dcat](https://github.com/ckan/ckanext-dcat)
* Activar el plugin en el fichero ini y reiniciar Apache2.
* Comprobación: Ir a cualquier conjunto de datos del portal y ver el código fuente de la página, todo será correcto si CKAN ha generado un texto del tipo

<pre>
<code>
  <script type="application/ld+json">
    {
    "@context": {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "schema": "http://schema.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#"
</code>        
</pre>

* Podremos buscar nuestro conjunto de datos en el buscador [Google Dataset Search](https://toolbox.google.com/datasetsearch) y el resultado será el conjunto de datos referenciando a nuestro portal de datos abiertos.

NOTA Importante: La indexación no es inmediata, por lo que hay que esperar unos días para que Google Dataset indexe nuestras páginas y aparezcan en el buscador.

## Licencia:

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias! 


![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


