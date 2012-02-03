# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from lib.common import striptag
from lib.common import add_class

from lib.forms import Login

from lib.auth import Cookie
from modules.User import User
from lib import httpagentparser as UA_Parser
_User = User('flame_user','local')

cookie = Cookie(_User)

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

class user(View):

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
		self.render = render_is(v)
		user = cookie.GET()
		if user:
			renderDict['user'] = user
			renderDict['path'] = "/static/themes/%s/%s" % (v,THEME)
			if page == "balance":
				return self.balance()
			if page == "analyse":
				return self.chart()
			if page == "briefing":
				return self.briefing()
		else:
			return web.seeother('/')
	
	def balance(self):
		from modules.Balance import Balance
		balance = Balance('flame_balance','local')
		renderDict['balances'] = balance.ShowAll(renderDict['user'].id)
		renderDict['left'] = balance.Left(renderDict['user'].id)
		return self.render.balance(renderDict)
	
	def chart(self):
		from modules.Record import Record
		record = Record('flame_record','local')
		import datetime
		d = datetime.date.today()
		strd = datetime.datetime.strftime(d, "%Y-%m-%d")
		strm = datetime.datetime.strftime(d, "%Y-%m")
		renderDict['pages'] = []
		PageList = renderDict['user'].list.split(',')
		for item in PageList:
			page = {}
			d_data = record.Get(strd,item,'day')
			m_data = record.Get(strm,item,'month')
			page['log'] = d_data[0]
			page['mlog'] = m_data[0]
			page['d'] = d_data[1]
			page['m'] = m_data[1]
			page['name'] = item
			renderDict['pages'].append(page)
		renderDict['name'] = renderDict['user'].nick
		return self.render.main(renderDict)
	
	def briefing(self):
		from modules.Balance import Balance
		balance = Balance('flame_balance','local')
		renderDict['total'] = balance.Total(renderDict['user'].id)
		renderDict['left'] = balance.Left(renderDict['user'].id)
		return self.render.briefing(renderDict)