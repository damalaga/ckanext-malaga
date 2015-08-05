# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
# 
# Funciones utiles para la federacion en datos.gob.es.
# Esta libreria la usa el fichero rdf para obtener datos


import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
import plugin as mlgplugin
import pylons.config as config 


# mlg_federador_value: Devuelve el valor estatico que 'val' tiene en el fichero .ini
# mlg_federador_value: Return 'val' static value on .ini file

def mlg_federador_value(val):
	return config[val]

# mlg_fed_total_resources_size: Devuelve la suma de bytes de todos los ficheros de recursos
# mlg_fed_total_resources_size: Returns bytes sum of resources
def mlg_fed_total_resources_size():

	siz = 0
	ds_list = mlgplugin.mlg_ds_list()
	for dsname in ds_list:
		data_dict = {'id':dsname}
		dsitem = toolkit.get_action('package_show')(data_dict=data_dict)
		for res in dsitem['resources']:
			if res['size'] is not None:
				siz = siz + int(res['size'])
	return siz

# mlg_fed_datasets_related: Devuelve los items relacionados con el dataset.
# Si dsname esta relleno, devuelve los items relacionados de ese dataset.
# Si dsname esta vacio, devuelve todos los items relacionados de todos los datasets.
# mlg_fed_datasets_related: Returns dataset related items.
# If dsname is filled, returns relations dataset called dsname. 
# If dsname is null, returns all relations datasets.

def mlg_fed_datasets_related(dsname):
	data_dict = {
		"id":dsname}
	related=toolkit.get_action('related_list')(data_dict=data_dict)
	return related

