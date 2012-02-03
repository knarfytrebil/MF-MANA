import os
import web

class View():
	"""docstring for ClassName"""
	def __init__(self):
		self.render = ""
	
	def render_is(self,v,THEME,SNIPPETS):
		TEMPLATE_PATH = '../templates/themes/%s/' % v
		app_root = os.path.abspath(os.path.join('..',os.path.dirname(__file__)))
		templates_root = os.path.join(app_root,TEMPLATE_PATH+THEME)
		return web.template.render(templates_root,globals=SNIPPETS)
	
	def agent_type(self):
		desktop = ['Linux','Windows','Macintosh','MacOS']
		try:
			s = web.ctx.env['HTTP_USER_AGENT']
		except KeyError:
			s = "Unknown"
		os = UA_Parser.simple_detect(s)
		print os[0].split(' ')[0]
		if os[0].split(' ')[0] not in desktop:
			return 'mobile'
		else:
			return 'desktop'