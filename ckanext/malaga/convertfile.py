import psycopg2

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

#comento esta linea para no tener que instalar por ahora dicttoxml en mv0115 ni en mv0112 
#from dicttoxml import dicttoxml

def _get_datastore(idds):
	
	data_dict = { 
		"resource_id": idds
	}
	return toolkit.get_action('datastore_search')(data_dict=data_dict) 

def csv_to_xml (idds):

	ds = _get_datastore(idds)
	return "nulo"
#comento esta linea para no tener que instalar por ahora dicttoxml en mv0115 ni en mv0112 
#	return dicttoxml(ds['records'],attr_type=False)
	
	
	
	


