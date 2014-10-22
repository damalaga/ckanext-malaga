import ckan.plugins as p
from ckan.lib.base import BaseController

class AplicacionesController(BaseController):
	def aplicaciones(self, apl_url):
		return p.toolkit.render(apl_url)


