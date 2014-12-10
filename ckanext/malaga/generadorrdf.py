# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
#

import ckan.plugins as p
from ckan.lib.base import BaseController

import federador as fed


# imports used on rdf render
import ckan.lib.accept as accept
from ckan.lib.base import response
from ckan.lib.base import (request,
                           render,
                           BaseController,
                           model,
                           abort, h, g, c)


class GenerarRDF(BaseController):


	def generar(self,fname, template):

		import os
		import sys

		datardf = render(template, loader_class=None)

		try:
			with open(fname, 'w') as f:
				f.write(datardf.encode('utf-8'))
				return p.toolkit.literal("proceso correcto")
		except IOError, ioe:
			sys.stderr.write( "Error !!!!! " + str(ioe) + "\n" )
			return p.toolkit.literal("error " + str(ioe))

