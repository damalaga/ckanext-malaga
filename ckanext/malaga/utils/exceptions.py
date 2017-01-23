# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
# @date		10-06-2016
#
# Usado para que los scripts sh muestre el error con detalle.
# Para usarlo en el sh hay que incluir la libreria y llamar 
# a este metodo pasandole la variable de sistema sys que tiene
# los errores
# Sh scripts use this to show error details. If you want to use 
# it you must include this library and call this method
# using system parameter sys which contains errors.
#
# from ckanext.malaga import exceptions
# except:
#	print exceptions.printExceptions(sys)




import traceback


def printExceptions(sys):

	  print '*******MENSAJES ESCRITOS DESDE ckanext.malaga.exceptions***********'

	  print '**************** Error en la actualizacion ****************'
	  exc_type, exc_value, exc_traceback = sys.exc_info()

	  print '***********************************'
	  print "*** Imprimiendo traceback.print_tb...saldra un error de stdin:" 
	  print '***********************************'
	  traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
	  print '..................................................'
	  
	  print '***********************************'
	  print "*** Imprimiendo traceback.print_exc:"
	  print '***********************************'
	  traceback.print_exc()
	  print '..................................................'

	  print '***********************************'
	  print "*** Imprimiendo format_exc, first and last line:"
	  print '***********************************'
	  formatted_lines = traceback.format_exc().splitlines()
	  print formatted_lines[0]
	  print formatted_lines[-1]
	  print '..................................................'


	  print '***********************************'
	  print "*** Imprimiendo format_exception:"
	  print '***********************************'
	  print repr(traceback.format_exception(exc_type, exc_value, exc_traceback))

	  print '..................................................'


	  print '***********************************'
	  print "*** Imprimiendo extract_tb:"
	  print '***********************************'
	  print repr(traceback.extract_tb(exc_traceback))
	  print '..................................................'

	  print '***********************************'
	  print "*** Imprimiendo format_tb:"
	  print '***********************************'
	  print repr(traceback.format_tb(exc_traceback))
	  print '..................................................'


