# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
# 


import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
import plugin as mlgplugin

# mlg_fed_total_resources_size: Devuelve la suma de bytes de todos los ficheros de recursos
# mlg_fed_total_resources_size: Returns bytes sum of resources
def mlg_fed_total_resources_size():
	datasets = mlgplugin.mlg_datasets_resources_list()
	count = 0
	for ds in datasets:
		for res in ds['resources']:
			count = count + int(res['size'] or 0)
	return count

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

