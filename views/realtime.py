# -*- coding: utf-8 -*-
import os
import web

from views.base import View
from modules.Access import Access
import json

class realtime(View):
	def GET(self,time):
		access = Access('flame_balance','local')	
		web.header('Content-Type', 'application/javascript')
		d = json.dumps({"address": "Shanghai", "tm": "00:00:00" })
		return 'gen_li(' + d + ');'