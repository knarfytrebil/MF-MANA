import os
import web

class View():
	"""docstring for ClassName"""
	def __init__(self):
		self.render = ""
	
	def render_is(v,THEME):
		TEMPLATE_PATH = '../templates/themes/%s/' % v
		THEME = 'user'
		SNIPPETS = {}
		SNIPPETS['strip'] = striptag
		SNIPPETS['addClass'] = add_class
		app_root = os.path.abspath(os.path.join('..',os.path.dirname(__file__)))
		templates_root = os.path.join(app_root,TEMPLATE_PATH+THEME)
		return web.template.render(templates_root,globals=SNIPPETS)