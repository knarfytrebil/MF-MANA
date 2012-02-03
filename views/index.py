# -*- coding: utf-8 -*-
import os
import web

from lib.common import striptag
from lib.common import add_class
from lib.forms import Login
from lib.auth import Cookie
from views.base import View

from modules.User import User


_User = User('flame_user')

cookie = Cookie(_User)

SNIPPETS = {}
SNIPPETS['strip'] = striptag
SNIPPETS['addClass'] = add_class

THEME = "user"
renderDict = {}

class index:
	def GET(self):
		v = self.agent_type()
		self.render = self.render_is(v,THEME,SNIPPETS)
		renderDict = {}
		user = cookie.GET()
		if user:
			return web.seeother('/user/briefing')
		else:
			title = "hello"
			renderDict = {'login':Login(),'name':'Stranger','title':title}
			return self.render.login(renderDict)

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
