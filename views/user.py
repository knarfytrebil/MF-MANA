# -*- coding: utf-8 -*-
import os
import web

from lib.common import striptag
from lib.common import add_class

from lib.forms import Login

from lib.auth import Cookie
from modules.User import User
from lib import httpagentparser as UA_Parser
_User = User('flame_user','local')

cookie = Cookie(_User)


v = "desktop"
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

class user:
	def GET(self,page):
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
		user = cookie.GET()
		if user:
			if page == "balance":
				from modules.Balance import Balance
				balance = Balance('flame_balance','local')
				renderDict['name'] = user.nick
				renderDict['balances'] = balance.ShowAll(user.id)
				renderDict['left'] = balance.Left(user.id)
				return render.balance(renderDict)
		else:
			return web.seeother('/')