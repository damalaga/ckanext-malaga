# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
#


import ckan.plugins as p

import os

import ckan.plugins.toolkit as toolkit
import ckan.lib.base as base

import urllib
import ckan.lib.helpers as ckanhelper

import operator #usado para ordenar los tags en orden ascendente // used asc tags order

import ast #usado para transformar un str a dict

#ckan2.4
# mlg_org_counter: Devuelve el numero de conjunto de datos asociados a la organizacion que se pasa en el id
# mlg_org_counter: Returns number of datasets in id organization

def mlg_organization_counter(id):
	data_dict = {'id':id,
		     'include_datasets':True}
	return toolkit.get_action('organization_show')(data_dict=data_dict)['package_count']

#ckan2.4
# mlg_group_counter: Devuelve el numero de conjunto de datos asociados a un grupo que se pasa en el id
# mlg_group_counter: Returns number of datasets in id group

def mlg_group_counter(id):
	data_dict = {'id':id,
		     'include_datasets':True}
	return toolkit.get_action('group_show')(data_dict=data_dict)['package_count']

#ckan2.3
# mlg_ds_list: Devuelve la lista de datasets 
# mlg_ds_list: Returns datasets name list
def mlg_ds_list():
	return toolkit.get_action('package_list')(data_dict={})

#ckan2.3	
# mlg_count_resources: Devuelve el numero de recursos.
# mlg_count_resources: Returns numbers of resources
def mlg_count_resources():
	ds = mlg_ds_list()
	count = 0
	for dsname in ds:
		data_dict = {'id':dsname}
		dsitem = toolkit.get_action('package_show')(data_dict=data_dict)
		count = count + dsitem['num_resources']
	return count

#ckan2.3
#mlg_top_tags: Devuelve las etiquetas más usadas, recibe el numero de etiquetas que tiene que devolver, si no recibe nada, devuelve 10 etiquetas.
# usa la libreria de estadisticas que trae ckan.
#mlg_top_tags: Returns most used tags, it recieve numbers of max tags to return, if not, by default, returns 10 tags.
# This function uses stats CKAN library.
def mlg_top_tags(showtags=10):
	import ckanext.stats.stats as ckanstats

	classtags = ckanstats.Stats()
	return classtags.top_tags(limit=showtags)

#ckan2.3
def mlg_ds_resources_list(dsname):

	data_dict = {'id':dsname}
	return toolkit.get_action('package_show')(data_dict=data_dict)
			

# mlg_tracking_summary: Recibe un identificador de dataset en iddataset
# devuelve el numero de visitas recientes (tracking_summary['recent'])
# y el numero total de visitas (tracking_summary['total'])
# mlg_tracking_summary: Get dataset id parameter iddataset
# returns numbers of recents visits (tracking_summary['recent'])
# and total visits (tracking_summary['total'])
def mlg_tracking_summary(iddataset):

	data_dict = {"id":iddataset,
		     "include_tracking":True}
	
	response = toolkit.get_action('package_show')(data_dict=data_dict)
	return response['tracking_summary']

# mlg_most_downloaded: Recibe el numero maximo de datasets que se van a devoler (_num_max)
# y el orden _order
# devuelve los datasets mas descargados
# mlg_most_downloaded: Get _num_max: number of datasets method will return _order: order by
# returns most downloaded datasets
def mlg_most_downloaded(_num_max, _order):

	data_dict = {"rows":_num_max,"sort":_order}
	
	response = toolkit.get_action('package_search')(data_dict=data_dict)
	return response['results']
# mlg_cur_datetime Devuelve la hora y fecha actual en formato YYYY-MM-DDTHH-MI-SS
# mlg_cur_datetime Returns current datetime, format YYYY-MM-DDTHH-MI-SS
def mlg_cur_datetime (self):
	from datetime import datetime, date, time
	today = str(datetime.now())
	return today[:10]+'T'+today[11:19]



# mlg_group_list: Devuelve una lista con los grupos
# mlg_group_list: Returns list of groups 
def mlg_group_list():
	data_dict = {'all_fields': True} #all_fields returns each group field (name, url, image,...).
	return toolkit.get_action('group_list')(data_dict=data_dict)

# mlg_organization_list Devuelve una lista con las organizaciones
# mlg_organization_list: Returns list of organization
def mlg_organization_list():
	data_dict = {'all_fields': True} #all_fields returns each group field (name, url, image,...).
	return toolkit.get_action('organization_list')(data_dict=data_dict)


class malagae(p.SingletonPlugin):

    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)


    p.implements(p.IRoutes, inherit=True)


#iruiz: Redefinir before_map para
# apl = nueva entrada en el menu, que se llama aplicaciones.

# Redefine before_map:
    def before_map(self, m):

	import pylons.config as config 

# Redefine before_map: incluye todos los pares URL redefinidas en el fichero ini:
	
		
	_mlgbeforemap = ast.literal_eval(config['ckan_mlg.before_map'])
	
	for _keybeforemap in _mlgbeforemap:
		m.connect(_keybeforemap, #name of path route
		'/'+_keybeforemap, #url to map path to
		controller='ckanext.malaga.controller:AplicacionesController', #controller
		action='printPage', apl_url=_mlgbeforemap[_keybeforemap]) #controller action (method)

		

	return m

    def update_config(self, config):
        # add template directory that contains our snippet
		p.toolkit.add_template_directory(config, '/usr/lib/ckan/default/src/ckanext-malaga/ckanext/malaga/theme/templates')
		p.toolkit.add_public_directory (config, '/usr/lib/ckan/default/src/ckanext-malaga/ckanext/malaga/public')

    #iruiz: register helper function
    def get_helpers(self):
        return {'mlg_count_resources':mlg_count_resources,
		'mlg_tracking_summary': mlg_tracking_summary,
		'mlg_most_downloaded': mlg_most_downloaded,
		'mlg_cur_datetime': mlg_cur_datetime,
		'mlg_group_list': mlg_group_list,
		'mlg_organization_list': mlg_organization_list,
		'mlg_ds_list': mlg_ds_list,
		'mlg_top_tags': mlg_top_tags,
		'mlg_ds_resources_list': mlg_ds_resources_list,
		'mlg_organization_counter': mlg_organization_counter,
		'mlg_group_counter': mlg_group_counter
}
