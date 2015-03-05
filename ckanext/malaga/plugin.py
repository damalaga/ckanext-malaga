# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
#


import ckan.plugins as p

import federador as fed

import os

import ckan.plugins.toolkit as toolkit
import ckan.lib.base as base

import urllib
import ckan.lib.helpers as ckanhelper

import operator #usado para ordenar los tags en orden ascendente // used asc tags order

# mlg_count_resources: Devuelve el numero de recursos.
# mlg_count_resources: Returns numbers of resources
def mlg_count_resources():

	data_dict = {}
	
	resources = toolkit.get_action('current_package_list_with_resources')(data_dict=data_dict)
	count = 0
	for resource in resources:
		count = count + resource['num_resources']

	return count

# mlg_tracking_summary: Recibe un identificador de dataset en iddataset
# devuelve el numero de visitas recientes (tracking_summary['recent'])
# y el numero total de visitas (tracking_summary['total'])
# mlg_tracking_summary: Get dataset id parameter iddataset
# returns numbers of recents visits (tracking_summary['recent'])
# and total visits (tracking_summary['total'])
def mlg_tracking_summary(iddataset):

	data_dict = {"id":iddataset}
	
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


# mlg_datasets_resources_list: Devuelve una lista de datasets con sus recursos
# mlg_datasets_resources_list: Returns a list of datasets and their resources
def mlg_datasets_resources_list():
	return toolkit.get_action('current_package_list_with_resources')(data_dict={})

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

# mlg_get_most_used_tags: Devuelve una lista de las etiquetas mas usadas y el numero de items que la usan
# mlg_get_most_used_tags: Returns list of the most used tags, and numbers of items
def mlg_get_most_used_tags(limit):
	lists = mlg_datasets_resources_list()
	hashtags = {}
	for ds in lists:
		if ds['tags']:
			for item in ds['tags']:
				if item['name']:
					if (item['name'] in hashtags):
						hashtags[item['name']] = hashtags[item['name']] + 1
					else:
						hashtags[item['name']] = 1

	return sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)[:limit]


class malagae(p.SingletonPlugin):

    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)


    p.implements(p.IRoutes, inherit=True)


#iruiz: Redefinir before_map para
# apl = nueva entrada en el menu, que se llama aplicaciones.
# federador = los ficheros que se usan en la federacion

# Redefine before_map:
    def before_map(self, m):

	import pylons.config as config 

# Redefine before_map: include aplicaciones on main menu
	apl_url_config = config['ckan_mlg.apl_url']                     #loading url ckan must open

	m.connect('aplicaciones', #name of path route
	'/aplicaciones', #url to map path to
	controller='ckanext.malaga.controller:AplicacionesController', #controller
	action='aplicaciones', apl_url=apl_url_config) #controller action (method)

# Redefine before_map: URL /local/generador execute GenerarRDF and generate rdf file used on datos.gob.es federacion
	federador_fname = config['ckan_mlg.federador_file']             #rdf filename (include path)
	federador_template = config['ckan_mlg.federador_template']      #loading rdf template filename (include path)
	federador_process = config['ckan_mlg.federador_process']        #federador process

	m.connect(federador_process, #name of path route
	'/'+federador_process, #url to map path to
	controller='ckanext.malaga.generadorrdf:GenerarRDF', #controller
	action='generar',fname=federador_fname, template=federador_template) #controller

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
		'mlg_fed_datasets_related': fed.mlg_fed_datasets_related,
		'mlg_fed_total_resources_size': fed.mlg_fed_total_resources_size,
		'mlg_group_list': mlg_group_list,
		'mlg_organization_list': mlg_organization_list,
		'mlg_datasets_resources_list': mlg_datasets_resources_list,
		'mlg_get_most_used_tags':mlg_get_most_used_tags,
		'mlg_federador_value':fed.mlg_federador_value
}
