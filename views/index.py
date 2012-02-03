# -*- coding: utf-8 -*-
import os
import web

from lib.common import striptag
from lib.common import add_class

from lib.forms import Login

from lib.auth import Cookie
from modules.User import User
from lib import httpagentparser as UA_Parser

_User = User('flame_user')

cookie = Cookie(_User)

v = ""
render = ''

def render_is(v):
	TEMPLATE_PATH = '../templates/themes/%s/' % v
	THEME = 'user'
	SNIPPETS = {}
	SNIPPETS['strip'] = striptag
	SNIPPETS['addClass'] = add_class
	app_root = os.path.abspath(os.path.join('..',os.path.dirname(__file__)))
	templates_root = os.path.join(app_root,TEMPLATE_PATH+THEME)
	return web.template.render(templates_root,globals=SNIPPETS)

desktop = ['Linux','Windows','Macintosh','MacOS']

renderDict = {}

class index:
	def GET(self):
		try:
			s = web.ctx.env['HTTP_USER_AGENT']
		except KeyError:
			s = "Unknown"
		os = UA_Parser.simple_detect(s)
		print os[0].split(' ')[0]
		if os[0].split(' ')[0] not in desktop:
			v = 'mobile'
		else:
			v = 'desktop'
		render = render_is(v)
		renderDict = {}
		user = cookie.GET()
		if user:
			return web.seeother('/user/briefing')
		else:
			title = "hello"
			renderDict = {'login':Login(),'name':'Stranger','title':title}
			return render.login(renderDict)

	def POST(self):
		login = Login()
		if not login.validates():
			return "Did not validate"
		else:
			#go and look for something in the database
			#change the cookie
			username = login.username.value
			password = login.password.value
			result = _User.BasicAuth(username,password)
			if result:
				uis = ",".join([result.name,result.password])
				cookie.SET(uis=uis)
				#render other page
				return web.seeother('/')
			else:
				return "Login Failed"
